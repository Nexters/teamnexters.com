<template>
  <div>
    <Header :headers="headers"></Header>
    <nuxt />
    <Footer></Footer>
  </div>
</template>

<script>
import { Component, Vue } from "nuxt-property-decorator";
import Header from "~/components/header.vue";

@Component({
  name: "default-layout",
  components: { Header },
  fetchOnServer: false,
  data() {
    return { headers: [] };
  },
  async fetch() {
    const { categories } = await this.$content("headers")
      .only(["categories"])
      .fetch();
    this.headers = categories;
  },
})
class DefaultLayout extends Vue {
  // headers?: string[]
}
export default DefaultLayout;
</script>
<style></style>
