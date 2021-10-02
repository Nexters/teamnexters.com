<template>
  <div>
    <Header :headers="headers"></Header>
    <nuxt />
    <Footer :items="items" :copyrights="copyrights"></Footer>
  </div>
</template>

<script>
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
class BaseLayout extends Vue {}
export default BaseLayout;
</script>
<style lang="scss" scoped></style>
