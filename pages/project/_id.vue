<template>
  <div class="container">
    <!-- <pre>{{ project }}</pre> -->
    <div class="contents">
      <div class="information">
        <h1 class="name">{{ project.app_name }}</h1>
        <div class="th-year">{{ project.th }} | {{ project.year }}</div>
        <div class="team-members">
          {{ project.team_name }} | {{ project.members.join(" ") }}
        </div>
      </div>
      <div class="thumbnail"><img :src="project.thumbnail" /></div>
      <div class="description">{{ project.description }}</div>
      <div class="ppt">
        <p>최종 발표 자료</p>
        <img src="~/assets/img/ic_forward_black.png" alt="arrow" />
      </div>
    </div>
    <div class="links">
      <a
        v-for="(link, platform) in project.link"
        :key="platform"
        class="link-item"
        :href="link"
      >
        {{ platform }}
      </a>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";
// import Project from "~/models/project";
export default defineComponent({
  name: "ProjectDetail",
  layout: "detail",
  async asyncData({ $content, params }) {
    console.debug(params);
    // console.log(extra);
    // 곧장 바로 들어온 경우 불러오지 못하므로 content에서 불러오도록 처리가 필요하다.
    // const project = Project.find(id);
    const [project] = await $content("_projects")
      .where({ idx: params.id })
      .fetch();
    console.log(project);
    return {
      project: project,
    };
  },
  data() {
    return {
      project: {},
    };
  },
  fetchOnServer: false,
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
* {
  font-family: Spoqa Han Sans Neo;
}

.container {
  height: calc(100% - 56px);
  display: flex;
  flex-direction: column;
}
.contents {
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.information {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.name {
  font-style: normal;
  font-weight: bold;
  font-size: 24px;
  line-height: 36px;
  letter-spacing: -0.02em;

  color: #000000;
}
.th-year {
  font-style: normal;
  font-weight: normal;
  font-size: 12px;
  line-height: 18px;
  letter-spacing: -0.02em;

  color: #777777;
}
.team-members {
  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: -0.02em;

  color: #000000;
}
.thumbnail {
  width: 100%;

  img {
    width: 100%;
    max-height: 445px;
    border-radius: 8px;
  }
}
.description {
  white-space: pre-wrap;

  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 21px;
  letter-spacing: -0.02em;

  color: #000000;
}
.ppt {
  display: flex;
  width: 130px;
  cursor: pointer;
  p {
    padding-right: 8px;
    font-style: normal;
    font-weight: bold;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: -0.02em;

    color: #000000;
  }
  img {
    width: 16px;
    height: 16px;
    margin: auto;
  }
}
a {
  text-decoration: none;
}
.links {
  margin-top: auto;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.link-item {
  font-weight: bold;
  font-size: 16px;
  line-height: 24px;
  text-align: center;
  letter-spacing: -0.02em;

  color: #000000;
  width: 100%;
  height: 45px;
  line-height: 45px;
  text-align: center;
  border: 1px solid #dddddd;
  margin-right: 8px;
  cursor: pointer;
}
.link-item:last-child {
  margin: 0;
}

@include desktop {
  .thumbnail {
    height: 445px;
  }
} ;
</style>
