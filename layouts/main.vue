<template>
  <div class="background">
    <Header :headers="headers" :is-white="true"></Header>
    <nuxt />
    <Footer :items="items" :copyrights="copyrights" :is-white="true"></Footer>
  </div>
</template>

<script>
import { useStore, computed } from "@nuxtjs/composition-api";
import { Component, Vue } from "nuxt-property-decorator";
import Header from "~/components/header.vue";
import Footer from "~/components/footer.vue";

@Component({
  name: "MainLayout",
  components: { Header, Footer },
  fetchOnServer: false,
  data() {
    return { headers: [], items: [], copyrights: "" };
  },
  setup() {
    const store = useStore();
    return {
      isMenuOpen: computed(() => store.state.isMenuOpen),
    };
  },
  async fetch() {
    const { headers } = await this.$content("headers")
      .only(["headers"])
      .fetch();
    const { items, copyrights } = await this.$content("footers")
      .only(["items", "copyrights"])
      .fetch();
    this.headers = headers;
    this.items = items;
    this.copyrights = copyrights;
  },
})
class MainLayout extends Vue {
  // headers?: string[]
}
export default MainLayout;
</script>
<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";
@import "~/assets/css/main-bg.scss";

.background {
  display: flex;
  flex-direction: column;
  @include desktop {
    background-image: $main-default-desktop;
  }
  @include tablet {
    background-image: $main-default-desktop;
  }
  @include mobile {
    background-image: $main-default-mobile;
  }
  background-size: cover;
  background-position: center;
  width: 100%;
  height: 100vh;
}
footer {
  color: $text-inverse;
}
</style>
