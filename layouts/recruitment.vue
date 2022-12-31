<template>
  <div class="background">
    <Header :headers="headers" :is-white="is_recruiting"></Header>
    <main>
      <nuxt v-if="!isMenuOpen || $mq !== 'mobile'" />
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

@Component({
  name: "RecruitmentLayout",
  fetchOnServer: false,
  data() {
    return {
      headers: [],
      items: [],
      copyrights: "",
      sponsors: [],
      recruitment_notice: "",
      recruitment_start: "",
      recruitment_end: "",
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
    const { recruitment_notice, recruitment_start, recruitment_end } =
      await this.$content("main")
        .only(["recruitment_notice", "recruitment_start", "recruitment_end"])
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

    const yymmdd = (date) => {
      return new Date(new Date(date).setHours(0, 0, 0, 0));
    };
    this.recruitment_notice = yymmdd(recruitment_notice);
    this.recruitment_start = yymmdd(recruitment_start);
    this.recruitment_end = yymmdd(recruitment_end);
  },
  computed: {
    s_day() {
      const result = new Date(this.recruitment_start) - new Date();
      return Math.ceil(result / 86400000);
    },
    d_day() {
      const result = new Date(this.recruitment_end) - new Date();
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
