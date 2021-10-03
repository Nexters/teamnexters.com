<template>
  <div class="container">
    <div class="contents">
      <div class="title">
        <h1>Look Around</h1>
        <div class="has-sup">
          <h1>Our Projects</h1>
          <sup v-if="projects.length > 0" class="total">{{
            projects.length
          }}</sup>
        </div>
      </div>
      <div class="project-container">
        <ProjectCard
          v-for="project in projects"
          :key="project.idx"
          class="project"
          :project="project"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";
import Project from "~/models/project";

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
    const _projects = await this.FetchAll();
    Project.create({ data: _projects });
    this.projects = _projects;
  },
  methods: {
    FetchAll: async function () {
      const { results } = await this.$content("projects")
        .only("results")
        .fetch();
      const { rawData } = results[0].result;
      const [_, ...projects] = rawData;
      console.debug(_);
      const _projects = projects.map((project) => this.Project(project));
      return _projects;
    },
    // Project object 생성자
    Project: function (columns) {
      if (columns.length != 12) {
        console.error(`프로젝트의 컬럼 수를 확인하세요: ${columns}`);
      }
      const [
        idx,
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
      let link = {};
      if (android_link.length > 0) {
        link["android"] = android_link;
      }
      if (ios_link.length > 0) {
        link["ios"] = ios_link;
      }
      if (web_link.length > 0) {
        link["web"] = web_link;
      }

      return {
        idx: idx,
        app_name: app_name,
        thumbnail: thumbnail_url,
        th: th + "th",
        year: year,
        team_name: team_name,
        members: members,
        description: description,
        ppt: ppt,
        link: link,
      };
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
* {
  font-family: Spoqa Han Sans Neo;
}
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
    gap: 48px;
    .project {
      flex-basis: 368px;
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
    gap: 48px;
    .project {
      flex-basis: 364.5px;
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
    gap: 24px;
    .project {
      flex-basis: 384px;
    }
  }
}

@include m-c1 {
  .contents {
    padding: 0 24px 0 24px;
    margin: 0 auto 0 auto;
    .title {
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
    display: flex;
    justify-content: space-between;
    box-sizing: border-box;
    flex-direction: column;
    gap: 24px;
    .project {
      flex-grow: 1;
    }
  }
}
</style>
