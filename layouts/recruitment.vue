<template>
  <div class="background">
    <Header :headers="headers" :is-white="is_recruiting"></Header>
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
    return {
      headers: [],
      items: [],
      copyrights: "",
      recruitment_notice: "",
      recruitment_start: "",
      recruitment_deadline: "",
    };
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
    const { recruitment_notice, recruitment_start, recruitment_deadline } =
      await this.$content("main")
        .only([
          "recruitment_notice",
          "recruitment_start",
          "recruitment_deadline",
        ])
        .fetch();
    this.headers = headers;
    this.items = items;
    this.copyrights = copyrights;
    const yymmdd = (date) => {
      return new Date(new Date(date).setHours(0, 0, 0, 0));
    };
    this.recruitment_notice = yymmdd(recruitment_notice);
    this.recruitment_start = yymmdd(recruitment_start);
    this.recruitment_deadline = yymmdd(recruitment_deadline);
  },
  computed: {
    s_day() {
      const result = new Date(this.recruitment_start) - new Date();
      return Math.ceil(result / 86400000);
    },
    d_day() {
      const result = new Date(this.recruitment_deadline) - new Date();
      return this.s_day < 0 ? Math.ceil(result / 86400000) : 0;
    },
    is_recruiting() {
      return this.s_day < 0 && this.d_day >= 0;
    },
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
