<template>
  <div class="background">
    <Header :headers="headers" :is-white="true"></Header>
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
  name: "RecruitmentLayout",
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
class RecruitmentLayout extends Vue {
  // headers?: string[]
}
export default RecruitmentLayout;
</script>
<style lang="scss" scoped>
.background {
  display: flex;
  width: 100%;
  flex-direction: column;
  height: 100vh;
}
</style>
