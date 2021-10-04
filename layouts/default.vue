<template>
  <div class="background">
    <Header :headers="headers" :is-white="false"></Header>
    <nuxt />
    <Footer :items="items" :copyrights="copyrights"></Footer>
  </div>
</template>

<script>
import { Component, Vue } from "nuxt-property-decorator";

@Component({
  name: "DefaultLayout",
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
