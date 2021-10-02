<template>
  <div class="container">
    <div class="contents">
      <div class="title">
        <h1>Look Around</h1>
        <div class="has-sup">
          <h1>Our Projects</h1>
          <sup class="total">{{ projects.length }}</sup>
        </div>
      </div>
      <div class="project-container">
        <div v-for="(project, idx) in projects" :key="idx" class="project">
          <img class="thumbnail" :src="project.thumbnail" />
          <p class="name">{{ project.app_name }}</p>
          <p class="time">{{ project.th }} | {{ project.year }}</p>
          <div class="link"></div>
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
      const thumbnail_url = `https://drive.google.com/uc?export=view&id=${thumbnail}`;
      return {
        app_name: app_name,
        thumbnail: thumbnail_url,
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
}

@include d-c3 {
  .contents {
    padding-top: 64px;
    width: 1200px;
    margin: 0 auto 0 auto;
    .title {
      display: flex;
      flex-direction: row;
      h1 {
        font-style: normal;
        font-weight: bold;
        font-size: 60px;
        line-height: 90px;
        letter-spacing: -0.02em;
      }
      .has-sup {
        display: flex;
        padding-left: 16px;
      }
      .total {
        font-style: normal;
        font-weight: normal;
        font-size: 24px;
        line-height: 36px;
        color: #000000;
        padding-left: 16px;
      }
    }
  }
  .project-container {
    padding-top: 32px;
    display: flex;
    justify-content: space-between;
    box-sizing: border-box;
    flex-direction: row;
    flex-wrap: wrap;
    .project {
      flex-basis: 30%;
      .thumbnail {
        width: 378px;
        height: 207px;
      }
      .name {
        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 36px;
        letter-spacing: -0.02em;
        color: #000000;
      }
      .time {
        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 21px;
        color: #777777;
      }
    }
  }
}

@include d-c2 {
  .contents {
    padding-top: 64px;
    width: 777px;
    margin: 0 auto 0 auto;
    .title {
      display: flex;
      flex-direction: column;
      h1 {
        font-style: normal;
        font-weight: bold;
        font-size: 60px;
        line-height: 90px;
        letter-spacing: -0.02em;
      }
      .has-sup {
        display: flex;
      }
      .total {
        font-style: normal;
        font-weight: normal;
        font-size: 24px;
        line-height: 36px;
        color: #000000;
        padding-left: 16px;
      }
    }
  }
  .project-container {
    padding-top: 32px;
    display: flex;
    justify-content: space-between;
    box-sizing: border-box;
    flex-direction: row;
    flex-wrap: wrap;
    .project {
      flex-basis: 49%;
      .thumbnail {
        width: 364.5px;
        height: 205px;
      }
      .name {
        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 36px;
        letter-spacing: -0.02em;
        color: #000000;
      }
      .time {
        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 21px;
        color: #777777;
      }
    }
  }
}

@include d-c1 {
  .contents {
    padding-top: 64px;
    width: 777px;
    margin: 0 auto 0 auto;
    .title {
      display: flex;
      flex-direction: column;
      h1 {
        font-style: normal;
        font-weight: bold;
        font-size: 60px;
        line-height: 90px;
        letter-spacing: -0.02em;
      }
      .has-sup {
        display: flex;
      }
      .total {
        font-style: normal;
        font-weight: normal;
        font-size: 24px;
        line-height: 36px;
        color: #000000;
        padding-left: 16px;
      }
    }
  }
  .project-container {
    padding-top: 32px;
    display: flex;
    justify-content: space-between;
    box-sizing: border-box;
    flex-direction: column;
    .project {
      flex-grow: 1;
      .thumbnail {
        width: 100%;
        height: 401px;
      }
      .name {
        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 36px;
        letter-spacing: -0.02em;
        color: #000000;
      }
      .time {
        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 21px;
        color: #777777;
      }
    }
  }
}

@include m-c2 {
  .contents {
    padding-top: 24px;
    width: 792px;
    margin: 0 auto 0 auto;
    .title {
      display: flex;
      h1 {
        font-style: normal;
        font-weight: bold;
        font-size: 32px;
        line-height: 48px;
        letter-spacing: -0.02em;
      }
      .has-sup {
        display: flex;
        padding-left: 10px;
      }
      .total {
        font-style: normal;
        font-weight: normal;
        font-size: 24px;
        line-height: 36px;
        color: #000000;
        padding-left: 8px;
      }
    }
  }
  .project-container {
    padding-top: 16px;
    display: flex;
    justify-content: space-between;
    box-sizing: border-box;
    flex-direction: row;
    flex-wrap: wrap;
    .project {
      flex-basis: 49%;
      .thumbnail {
        width: 100%;
        height: 216px;
      }
      .name {
        font-style: normal;
        font-weight: bold;
        font-size: 16px;
        line-height: 24px;
        letter-spacing: -0.02em;
        color: #000000;
      }
      .time {
        font-style: normal;
        font-weight: normal;
        font-size: 12px;
        line-height: 18px;
        color: #777777;
      }
    }
  }
}

@include m-c1 {
  .contents {
    width: 327px;
    margin: 0 auto 0 auto;
    .title {
      padding: 24px 24px 0 24px;
      display: flex;
      flex-direction: column;
      h1 {
        font-style: normal;
        font-weight: bold;
        font-size: 32px;
        line-height: 48px;
        letter-spacing: -0.02em;
      }
      .has-sup {
        display: flex;
      }
      .total {
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        line-height: 36px;
        color: #000000;
        padding-left: 8px;
      }
    }
  }
  .project-container {
    padding: 16px 24px 0 24px;
    display: flex;
    justify-content: space-between;
    box-sizing: border-box;
    flex-direction: column;
    .project {
      flex-grow: 1;
      .thumbnail {
        width: 100%;
        height: 216px;
      }
      .name {
        font-style: normal;
        font-weight: bold;
        font-size: 16px;
        line-height: 24px;
        letter-spacing: -0.02em;
        color: #000000;
      }
      .time {
        font-style: normal;
        font-weight: normal;
        font-size: 12px;
        line-height: 18px;
        color: #777777;
      }
    }
  }
}
</style>
