<template>
  <div>
    <Header></Header>
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
  async fetch() {
    let headers = await this.$content("headers").fetch();
    let about = await this.$content("about").only(["title"]).fetch();
    console.log(this);
    console.log(headers);
    console.log(about);
  },
})
class DefaultLayout extends Vue {
  // headers?: string[]
}
export default DefaultLayout;
</script>
<style></style>
