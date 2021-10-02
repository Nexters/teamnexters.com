<template>
  <div class="background">
    <Header :headers="headers" :is-white="true"></Header>
    <nuxt />
    <Footer :items="items" :copyrights="copyrights" :is-white="true"></Footer>
  </div>
</template>

<script>
import { Component, Vue } from "nuxt-property-decorator";
import Header from "~/components/header.vue";
import Footer from "~/components/footer.vue";

@Component({
  name: "default-layout",
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
class DefaultLayout extends Vue {
  // headers?: string[]
}
export default DefaultLayout;
</script>
<style lang="scss" scoped>
.background {
  display: flex;
  flex-direction: column;
  background-image: url("~/assets/img/main_bg.png");
  background-size: cover;
  background-position: 100%;
  width: 100%;
  height: 100vh;
}
footer {
  color: #ffffff;
}
</style>
