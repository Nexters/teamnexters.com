<template>
  <div class="background">
    <Header :headers="headers" :is-white="false"></Header>
    <main>
      <nuxt v-if="!isMenuOpen || $mq !== 'mobile'" />
    </main>
    <Footer :items="items" :copyrights="copyrights"></Footer>
  </div>
</template>

<script>
import { useStore, computed } from "@nuxtjs/composition-api";
import { Component, Vue } from "nuxt-property-decorator";

@Component({
  name: "DefaultLayout",
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
    const items = await this.$content("footers/sns")
      .only(["idx", "name", "href", "black", "white", "visible"])
      .fetch();
    const { copyrights } = await this.$content("footers/copyrights")
      .only(["copyrights"])
      .fetch();

    this.headers = headers;
    this.items = items;
    this.copyrights = copyrights;
  },
})
class DefaultLayout extends Vue {
  // headers?: string[]
}
export default DefaultLayout;
</script>
<style lang="scss" scoped>
.background {
  display: flex;
  width: 100%;
  flex-direction: column;
  height: 100vh;
}
</style>
