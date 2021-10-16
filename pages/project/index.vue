<template>
  <transition name="project">
    <div class="project-container">
      <ProjectDetail :project="project" />
      <div class="contents">
        <div class="title">
          <h1>Look Around</h1>
          <div class="has-sup">
            <h1>Our Projects</h1>
            <sup v-if="total > 0" class="total">{{ total }}</sup>
          </div>
        </div>
        <div class="project-cards-container">
          <ProjectCard
            v-for="_project in projects"
            :key="_project.idx"
            class="project"
            :project="_project"
          />
        </div>
        <div class="lead-more" @click="onClickMore">
          <p>Lead more</p>
          <img src="~/assets/img/ic_down.png" alt="" />
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
import { mapActions, mapGetters } from "vuex";

export default defineComponent({
  name: "Project",
  transition: {
    name: "project",
  },
  async asyncData({ $content }) {
    const projects = await $content("projects")
      .sortBy("idx")
      .limit(3)
      .fetch()
      .catch((err) => {
        console.log(err);
      });
    const { length } = await $content("projects").fetch();

    return {
      projects: projects,
      total: length,
    };
  },
  fetchOnServer: false,
  data() {
    return { total: 0, projects: [] };
  },
  computed: {
    ...mapGetters({
      project: "project/project",
      showDetail: "project/showDetail",
    }),
  },
  methods: {
    ...mapActions({
      showDetail: "project/showDetail",
    }),
    async onClickMore() {
      const projects = await this.$content("projects").sortBy("idx").fetch();
      this.projects = projects;
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
* {
  font-family: Spoqa Han Sans Neo;
}
.project-enter-active,
.project-leave-active {
  transition: opacity 1.5s;
}
.project-enter,
.project-leave-active {
  opacity: 0;
}
body.scroll-hidden {
  overflow-y: hidden;
}
.project-container {
  width: 100%;
  margin: 0 auto 0 auto;

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
    .project-cards-container {
      padding-top: 32px;
      display: flex;
      justify-content: space-between;
      box-sizing: border-box;
      flex-direction: row;
      flex-wrap: wrap;
      gap: 48px;
      .project {
        flex-basis: 360px;
        border-radius: 16px;
      }
    }
    .lead-more {
      margin: 24px auto 64px auto;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 155px;
      height: 68px;
      font-weight: bold;
      font-size: 24px;
      line-height: 36px;
      letter-spacing: -0.02em;
      color: #000000;
      img {
        margin-left: 9.33px;
        width: 20px;
        height: 11px;
      }
    }
  }

  @include d-c2 {
    .contents {
      padding: 64px 64px 0 64px;
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
    .project-cards-container {
      padding-top: 32px;
      display: flex;
      justify-content: space-between;
      box-sizing: border-box;
      flex-direction: row;
      flex-wrap: wrap;
      gap: 48px;
      .project {
        flex-basis: 362px;
        border-radius: 16px;
      }
    }
    .lead-more {
      margin: 24px auto 64px auto;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 155px;
      height: 68px;
      font-weight: bold;
      font-size: 24px;
      line-height: 36px;
      letter-spacing: -0.02em;
      color: #000000;
      img {
        margin-left: 9.33px;
        width: 20px;
        height: 11px;
      }
    }
  }

  @include d-c1 {
    .contents {
      padding: 24px 64px 0 64px;
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
    .project-cards-container {
      padding-top: 32px;
      display: flex;
      justify-content: space-between;
      box-sizing: border-box;
      flex-direction: column;
      gap: 48px;
      .project {
        flex-grow: 1;
        border-radius: 16px;
      }
    }
    .lead-more {
      margin: 24px auto 64px auto;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 155px;
      height: 68px;
      font-weight: bold;
      font-size: 24px;
      line-height: 36px;
      letter-spacing: -0.02em;
      color: #000000;
      img {
        margin-left: 9.33px;
        width: 20px;
        height: 11px;
      }
    }
  }

  @include m-c2 {
    .contents {
      width: 100%;
      .title {
        display: flex;
        padding-left: 16px;
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
    .project-cards-container {
      padding: 16px 24px 0 24px;
      margin: 0 auto 0 auto;
      display: flex;
      width: 792px;
      justify-content: space-between;
      box-sizing: border-box;
      flex-direction: row;
      flex-wrap: wrap;
      gap: 24px;
      .project {
        flex-basis: 358px;
        border-radius: 8px;
      }
    }
    .lead-more {
      margin: 24px auto 64px auto;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 106px;
      height: 40px;
      font-weight: bold;
      font-size: 16px;
      line-height: 24px;
      letter-spacing: -0.02em;
      color: #000000;
      img {
        margin-left: 9.33px;
        width: 13.33px;
        height: 7.33px;
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
    .project-cards-container {
      display: flex;
      justify-content: space-between;
      box-sizing: border-box;
      flex-direction: column;
      gap: 24px;
      .project {
        flex-grow: 1;
        border-radius: 8px;
      }
    }
    .lead-more {
      margin: 24px auto 64px auto;
      cursor: pointer;
      display: flex;
      justify-content: center;
      align-items: center;
      width: 106px;
      height: 40px;
      font-weight: bold;
      font-size: 16px;
      line-height: 24px;
      letter-spacing: -0.02em;
      color: #000000;
      img {
        margin-left: 9.33px;
        width: 13.33px;
        height: 7.33px;
      }
    }
  }
}
</style>
