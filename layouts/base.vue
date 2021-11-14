<template>
  <div>
    <Header :headers="headers"></Header>
    <main>
      <nuxt v-if="$mq !== 'mobile' || !isMenuOpen" />
    </main>
    <Footer :items="items" :copyrights="copyrights"></Footer>
  </div>
</template>

<script>
import { useStore, computed } from "@nuxtjs/composition-api";
import { Component, Vue } from "nuxt-property-decorator";
import Header from "~/components/header.vue";
import Footer from "~/components/footer.vue";

@Component({
  name: "BaseLayout",
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
    const items = await this.$content("footers/sns")
      .only(["idx", "name", "href", "black", "white"])
      .fetch();
    const copyrights = this.$content("footers/copyrights")
      .only(["copyrights"])
      .fetch();

    this.headers = headers;
    this.items = items;
    this.copyrights = copyrights;
  },
})
class BaseLayout extends Vue {}
export default BaseLayout;
</script>
<style lang="scss" scoped></style>
