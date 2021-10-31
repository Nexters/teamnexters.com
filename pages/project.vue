<template>
  <transition name="project">
    <div class="project-container">
      <ProjectDetail :project="project" />
      <div class="contents">
        <div class="title">
          <h2>Look Around</h2>
          <div class="has-sup">
            <h2>Our Projects</h2>
            <sup v-if="total > 0" class="total">{{ total }}</sup>
          </div>
        </div>
        <div class="project-cards-container">
          <div class="project-cards">
            <ProjectCard
              v-for="_project in projects"
              :key="_project.idx"
              class="project"
              :project="_project"
            />
          </div>
          <div v-show="isRemain" class="more">
            <div class="lead-more" @click="onClickMore">
              <p>Load more</p>
              <img src="~/assets/img/ic_down.svg" alt="" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
import { mapGetters, mapActions } from "vuex";

export default defineComponent({
  name: "Project",
  transition: {
    name: "project",
  },
  async asyncData({ $content }) {
    const projects = await $content("projects")
      .sortBy("idx", "desc")
      .limit(6)
      .fetch()
      .catch((err) => {
        console.log(err);
      });
    const { length } = await $content("projects").fetch();

    return {
      projects: projects,
      more: true,
      total: length,
    };
  },
  fetchOnServer: false,
  data() {
    return { total: 0, projects: [], more: true };
  },
  computed: {
    ...mapGetters({
      project: "project/project",
      showDetailFromStore: "project/showDetail",
      projectLimitFromStore: "project/projectLimit",
    }),
    showDetail: {
      get() {
        return this.showDetailFromStore;
      },
      set(value) {
        return this.setShowDetail(value);
      },
    },
    projectLimit: {
      get() {
        return this.projectLimitFromStore;
      },
      set(limit) {
        return this.setProjectLimit(limit);
      },
    },
    isRemain: {
      get() {
        return this.projectLimit < this.total;
      },
    },
  },
  methods: {
    ...mapActions({
      setShowDetail: "project/showDetail",
      setProjectLimit: "project/projectLimit",
    }),
    async onClickMore() {
      if (this.isRemain) {
        this.projectLimit += 6;
      } else {
        this.more = false;
      }
      const projects = await this.$content("projects")
        .sortBy("idx", "desc")
        .limit(this.projectLimit)
        .fetch();
      this.projects = projects;
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";

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
  margin: 73px auto 0 auto;

  @include d-c3 {
    .contents {
      padding-top: 64px;
      width: 1200px;
      margin: 73px auto 0 auto;
      .title {
        display: flex;
        flex-direction: row;
        h2 {
          font-style: normal;
          font-weight: bold;
          font-size: 48px;
          line-height: 64px;
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
          color: $text-default;
          padding-left: 16px;
        }
      }
    }
    .project-cards-container {
      display: flex;
      flex-direction: column;
      margin-bottom: 120px;
      .project-cards {
        display: flex;
        justify-content: space-between;
        box-sizing: border-box;
        flex-direction: row;
        flex-wrap: wrap;
        .project {
          margin-top: 48px;
          flex-basis: 365px;
          border-radius: 16px;
        }
      }
      .more {
        margin-top: 48px;
        .lead-more {
          margin: 0 auto 0 auto;
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
          color: $text-default;
          img {
            margin-left: 9.33px;
            width: 20px;
            height: 11px;
          }
        }
      }
    }
  }

  @include d-c2 {
    .contents {
      padding: 64px 0 0 0;
      margin: 0 64px 0 64px;
      .title {
        display: flex;
        flex-direction: column;
        h2 {
          font-style: normal;
          font-weight: bold;
          font-size: 48px;
          line-height: 64px;
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
          color: $text-default;
          padding-left: 16px;
        }
      }
    }
    .project-cards-container {
      display: flex;
      flex-direction: column;
      margin-bottom: 120px;
      .project-cards {
        padding-top: 84px;
        display: flex;
        justify-content: space-between;
        box-sizing: border-box;
        flex-direction: row;
        flex-wrap: wrap;
        .project {
          margin-top: 48px;
          flex-basis: calc(50% - 26px);
          border-radius: 16px;
        }
      }
      .more {
        margin-top: 48px;
        display: flex;
        justify-content: center;
        align-items: center;
        .lead-more {
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
          color: $text-default;
          img {
            margin-left: 9.33px;
            width: 20px;
            height: 11px;
          }
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
        h2 {
          font-style: normal;
          font-weight: bold;
          font-size: 48px;
          line-height: 64px;
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
          color: $text-default;
          padding-left: 16px;
        }
      }
    }
    .project-cards-container {
      display: flex;
      flex-direction: column;
      margin-bottom: 120px;
      .project-cards {
        display: flex;
        justify-content: space-between;
        box-sizing: border-box;
        flex-direction: column;
        .project {
          margin-top: 48px;
          flex-grow: 1;
          border-radius: 16px;
        }
      }
      .more {
        margin-top: 48px;
        display: flex;
        justify-content: center;
        align-items: center;
        .lead-more {
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
          color: $text-default;
          img {
            margin-left: 9.33px;
            width: 20px;
            height: 11px;
          }
        }
      }
    }
  }

  @include m-c2 {
    .contents {
      width: 100%;
      .title {
        display: flex;
        padding-left: 24px;
        h2 {
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
          font-size: 16px;
          line-height: 24px;
          color: $text-default;
          padding-left: 8px;
        }
      }
    }
    .project-cards-container {
      display: flex;
      flex-direction: column;
      margin-bottom: 24px;
      .project-cards {
        padding: 16px 24px 0 24px;
        display: flex;
        justify-content: space-between;
        box-sizing: border-box;
        flex-direction: row;
        flex-wrap: wrap;
        .project {
          margin-bottom: 24px;
          flex-basis: calc(50% - 14px);
          border-radius: 8px;
        }
      }
      .more {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 0 0 60px 0;
        .lead-more {
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
          color: $text-default;
          img {
            margin-left: 9.33px;
            width: 13.33px;
            height: 7.33px;
          }
        }
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
        h2 {
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
          line-height: 24px;
          color: $text-default;
          padding-left: 8px;
        }
      }
    }
    .project-cards-container {
      display: flex;
      flex-direction: column;
      margin-bottom: 24px;
      .project-cards {
        margin-bottom: 24px;
        display: flex;
        justify-content: space-between;
        box-sizing: border-box;
        flex-direction: column;
        .project {
          margin-top: 24px;
          flex-grow: 1;
          border-radius: 8px;
        }
      }
      .more {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 64px;
        .lead-more {
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
          color: $text-default;
          img {
            margin-left: 9.33px;
            width: 13.33px;
            height: 7.33px;
          }
        }
      }
    }
  }
}
</style>
