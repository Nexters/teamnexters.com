<template>
  <div class="container">
    <div class="contents">
      <div class="title">
        <div>
          <h1>Look Around</h1>
        </div>
        <div>
          <h1>Our Projects</h1>
        </div>
        <div class="total">
          <p>{{ projects.length }}</p>
        </div>
      </div>
      <div class="projects">
        <div v-for="(project, idx) in projects" :key="idx" class="project">
          <img :src="project.thumbnail" :alt="project.app_name" />
          <p>{{ project.app_name }}</p>
          <p>{{ project.th }} | {{ project.year }}</p>
          <p></p>
          <br />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Project",
  fetchOnServer: false,
  setup() {
    return {};
  },
  data() {
    return { projects: [] };
  },
  async fetch() {
    const { results } = await this.$content("projects").only("results").fetch();
    const { rawData } = results[0].result;
    console.log(rawData);
    const [_, ...projects] = rawData;
    this.projects = projects.map((project) => this.Project(project));
  },
  methods: {
    // Project object 생성자
    Project: function (columns) {
      if (columns.length != 11) {
        console.error(`프로젝트의 컬럼 수를 확인하세요: ${columns}`);
      }
      const [
        app_name,
        thumbnail,
        th,
        year,
        team_name,
        _members,
        description,
        ppt,
        android_link,
        ios_link,
        web_link,
      ] = columns;

      const members = _members.split(",").map((member) => member.trim());
      return {
        app_name: app_name,
        thumbnail: thumbnail,
        th: th + "th",
        year: year,
        team_name: team_name,
        members: members,
        description: description,
        ppt: ppt,
        android_link: android_link,
        ios_link: ios_link,
        web_link: web_link,
      };
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
.container {
  width: 100%;
  .contents {
    width: 1200px;
    margin: 0 auto 0 auto;
    .title {
      display: flex;
      flex-direction: row;
      h1:first-child {
        padding-right: 10px;
      }
      h1 {
        font-style: normal;
        font-weight: bold;
        font-size: 60px;
        line-height: 90px;
        /* identical to box height, or 150% */

        letter-spacing: -0.02em;
      }
      .total {
        font-style: normal;
        font-weight: normal;
        font-size: 24px;
        line-height: 36px;
        /* identical to box height, or 150% */

        /* text/default */

        color: #000000;
      }
    }
  }
}
</style>
