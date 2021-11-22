<template>
  <div>
    <Header :headers="headers"></Header>
    <main>
      <nuxt v-if="$mq !== 'mobile' || !isMenuOpen" />
    </main>
    <Footer
      :items="items"
      :copyrights="copyrights"
      :sponsors="sponsors"
    ></Footer>
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
    return { headers: [], items: [], copyrights: "", sponsors: [] };
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
    const sponsors = await this.$content("footers/sponsor")
      .only(["idx", "name", "href", "isVisible"])
      .fetch();
    this.headers = headers;
    this.items = items;
    this.copyrights = copyrights;
    this.sponsors = sponsors.filter((sponsor) => sponsor.isVisible);
  },
})
class BaseLayout extends Vue {}
export default BaseLayout;
</script>
<style lang="scss" scoped></style>
