<template>
  <div
    class="background"
    :style="{
      'background-image': background_image,
      'background-size': 'cover',
      'background-position': 'center',
    }"
  >
    <Header :headers="headers" :is-white="true"></Header>
    <nuxt />
    <Footer :items="items" :copyrights="copyrights" :is-white="true"></Footer>
  </div>
</template>

<script>
import { useStore, computed } from "@nuxtjs/composition-api";
import { Component, Vue } from "nuxt-property-decorator";
import Header from "~/components/header.vue";
import Footer from "~/components/footer.vue";
import background from "~/assets/css/export.scss";

@Component({
  name: "MainLayout",
  components: { Header, Footer },
  fetchOnServer: false,
  data() {
    return {
      headers: [],
      items: [],
      copyrights: "",
      recruitment_notice: "",
      recruitment_start: "",
      recruitment_deadline: "",
      ...background,
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
    this.recruitment_notice = recruitment_notice;
    this.recruitment_start = recruitment_start;
    this.recruitment_deadline = recruitment_deadline;
  },
  computed: {
    notice_day() {
      const result = new Date(this.recruitment_notice) - new Date();
      return Math.floor(result / 86400000);
    },
    s_day() {
      const result = new Date(this.recruitment_start) - new Date();
      return Math.floor(result / 86400000);
    },
    d_day() {
      const result = new Date(this.recruitment_deadline) - new Date();
      return this.s_day < 0 ? Math.floor(result / 86400000) : 0;
    },
    before_recruitment() {
      return this.notice_day < 0 && this.s_day >= 0;
    },
    is_recruiting() {
      return this.s_day < 0 && this.d_day >= 0;
    },
    background_image() {
      let img = this.main_default_desktop;
      if (this.before_recruitment) {
        img = this.main_notice_desktop;
      } else if (this.is_recruiting) {
        img = this.main_wip_desktop;
      }
      return img;
    },
  },
})
class MainLayout extends Vue {
  // headers?: string[]
}
export default MainLayout;
</script>
<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";
@import "~/assets/css/main-bg.scss";

.background {
  display: flex;
  flex-direction: column;
  background-size: cover;
  background-position: center;
  width: 100%;
  height: 100vh;
}
footer {
  color: $text-inverse;
}
</style>
