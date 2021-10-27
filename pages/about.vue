<template>
  <transition name="about" mode="out-in">
    <div class="about-container">
      <div class="slogan">
        <h1 class="slogan-text">{{ slogan }}</h1>
      </div>
      <div class="info-table">
        <div class="info-row">
          <h2 class="title">{{ info.title }}</h2>
          <div class="information">
            <div class="cards">
              <!-- <pre>{{ informations }}</pre> -->
              <InfoCard
                v-for="item in info.items"
                :key="item.title"
                :title="item.title"
                :value="item.value"
                :description="item.description"
              />
            </div>
          </div>
        </div>
      </div>
      <div class="contents">
        <!-- horizontal scroll -->
        <div class="activity-row">
          <div class="activities">
            <h2 class="title">{{ act.title }}</h2>
            <h3 class="desc">{{ act.desc }}</h3>
            <div class="cards">
              <ActivityCard
                v-for="item in act.items"
                :key="item.title"
                :description="item.description"
                :title="item.title"
                :thumbnail="item.thumbnail"
              />
            </div>
          </div>
        </div>
        <div class="review-row">
          <div class="reviews">
            <h2 class="title">{{ review.title }}</h2>
            <div class="cards">
              <ReviewCard
                v-for="item in review.items"
                :key="item.id"
                :th="item.th"
                :th-background-color="item.thBackgroundColor"
                :th-text-color="item.thTextColor"
                :title="item.title"
                :author="item.author"
                :href="item.href"
              />
            </div>
            <div
              class="more"
              :style="`${review.more || 'margin-bottom: 60px;'}`"
            >
              <div
                class="lead-more"
                :style="`display: ${review.more ? 'flex' : 'none'};`"
                @click="onClickMore"
              >
                <p>Lead more</p>
                <img src="~/assets/img/ic_down.svg" alt="" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";

export default defineComponent({
  name: "AboutPage",
  transition: {
    name: "about",
  },
  async asyncData({ $content }) {
    const {
      slogan,
      info_title,
      info_desc,
      activity_title,
      activity_desc,
      review_title,
      review_desc,
    } = await $content("about/text")
      .only([
        "slogan",
        "info_title",
        "info_desc",
        "activity_title",
        "activity_desc",
        "review_title",
        "review_desc",
      ])
      .fetch();
    const informations = await $content("about/informations")
      .only(["title", "value", "description"])
      .fetch();
    const activities = await $content("about/activities")
      .only(["description", "title", "thumbnail"])
      .fetch();
    const reviews = await $content("about/reviews")
      .only([
        "id",
        "th",
        "thBackgroundColor",
        "thTextColor",
        "title",
        "author",
        "href",
      ])
      .sortBy("id")
      .limit(6)
      .fetch()
      .catch((err) => {
        console.log(err);
      });
    return {
      slogan: slogan,
      info: {
        title: info_title,
        desc: info_desc,
        items: informations,
      },
      act: {
        title: activity_title,
        desc: activity_desc,
        items: activities,
      },
      review: {
        title: review_title,
        desc: review_desc,
        items: reviews,
        more: true,
      },
    };
  },
  data() {
    return {
      slogan: "",
      info: {
        title: "10년째\n멈추지 않는 열정",
        items: [],
      },
      act: {
        title: "함께하는\n다양한 활동",
        description:
          "정규 활동은 방학 시즌 매주 토요일에 진행되며,\n비활동 기간에는 프로젝트 · 공모전 · 스터디를 자율적으로 진행합니다.",
        items: [],
      },
      review: {
        title: "회원들의\n생생한 활동 후기",
        items: [],
        more: true,
      },
    };
  },
  methods: {
    async onClickMore() {
      const reviews = await this.$content("about/reviews")
        .sortBy("id")
        .fetch()
        .catch((err) => {
          console.log(err);
        });
      this.review.items = reviews;
      this.review.more = false;
    },
  },
  fetchOnServer: false,
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/color.scss";

* {
  font-family: Spoqa Han Sans Neo;
}
.about-enter-active,
.about-leave-active {
  transition: opacity 1.5s;
}
.about-enter,
.about-leave-active {
  opacity: 0;
}

.slogan {
  display: flex;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;

  padding-top: 73px;
}

.about-container {
  @include desktop {
    .contents {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      grid-gap: 64px;
      width: 100%;
      margin: 0 auto 0 auto;
    }
    .slogan {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      width: 100%;
      height: 809px;
      background: $grey01;
      margin-bottom: 120px;
      h1 {
        width: 1200px;
        white-space: pre-wrap;
        font-style: normal;
        font-weight: normal;
        font-size: 24px;
        line-height: 36px;

        text-align: center;
        letter-spacing: -0.02em;

        color: $grey03;
      }
    }
    .title {
      font-style: normal;
      font-weight: bold;
      font-size: 48px;
      line-height: 64px;
      letter-spacing: -0.02em;
      white-space: pre-wrap;

      color: $black;
    }
    .info-table {
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-bottom: 120px;
      .info-row {
        display: flex;
        flex-direction: column;
        justify-content: center;
      }
      .information {
        margin-top: 42px;
        width: 1200px;
        display: flex;
        flex-direction: column;
        .cards {
          display: flex;
          justify-content: space-between;
        }
      }
    }
    .activity-row {
      display: flex;
      justify-content: center;
    }
    .activities {
      display: flex;
      flex-direction: column;
      width: 1200px;
      grid-gap: 32px;
      .desc {
        font-style: normal;
        font-weight: normal;
        font-size: 24px;
        line-height: 36px;
        letter-spacing: -0.02em;
        white-space: pre-wrap;
        color: $text-default;
      }
      .cards {
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        grid-gap: 32px;
      }
    }
    .review-row {
      display: flex;
      justify-content: center;
    }
    .reviews {
      display: flex;
      flex-direction: column;
      width: 1200px;
      .cards {
        margin-top: 48px;
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        grid-gap: 32px;
      }
      .more {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 48px 0 120px 0;
        .lead-more {
          display: flex;
          justify-content: space-between;
          align-items: center;
          width: 155px;
          height: 68px;
          cursor: pointer;
          font-style: normal;
          font-weight: bold;
          font-size: 24px;
          line-height: 36px;
          letter-spacing: -0.02em;
          color: $text-default;
        }
      }
    }
  }
  @include tablet {
    .contents {
      display: flex;
      flex-direction: column;
      width: calc(100% - 128px);
      margin: 0 auto 0 auto;
      padding: 0 64px 0 64px;
    }
    .slogan {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      height: 809px;
      background: $grey01;
      margin-bottom: 120px;
      .slogan-text {
        white-space: pre-wrap;
        font-style: normal;
        font-weight: normal;
        font-size: 24px;
        line-height: 36px;

        text-align: center;
        letter-spacing: -0.02em;

        color: $grey03;
      }
    }
    .title {
      font-style: normal;
      font-weight: bold;
      font-size: 48px;
      line-height: 64px;
      letter-spacing: -0.02em;
      white-space: pre-wrap;

      color: $black;
    }
    .info-table {
      .info-row {
        display: flex;
        flex-direction: column;
        margin-bottom: 120px;
        .title {
          padding-left: 64px;
        }
        .information {
          margin-top: 48px;
          overflow-x: auto;
          scrollbar-width: none;
          -ms-overflow-style: none;
          -webkit-overflow-scrolling: touch;
          &::-webkit-scrollbar {
            display: none;
          }
          display: flex;
          flex-direction: column;
          .cards {
            min-width: 1200px;
            // grid-gap: 32px;
            justify-content: space-between;
            display: inline-flex;
            flex: 0 0 auto;
            padding: 0 64px 0 64px;
          }
        }
      }
    }
    .activity-row {
      display: flex;
    }
    .activities {
      display: flex;
      flex-direction: column;
      grid-gap: 32px;
      .desc {
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        line-height: 24px;
        letter-spacing: -0.02em;
        white-space: pre-wrap;
        color: $text-default;
      }
      .cards {
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        grid-gap: 32px;
      }
    }
    .review-row {
      display: flex;
      justify-content: center;
      margin-top: 120px;
    }
    .reviews {
      display: flex;
      flex-direction: column;
      grid-gap: 32px;
      .cards {
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        grid-gap: 32px;
      }
      .more {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 120px;
        .lead-more {
          display: flex;
          justify-content: space-between;
          align-items: center;
          width: 155px;
          height: 68px;
          cursor: pointer;
          font-style: normal;
          font-weight: bold;
          font-size: 24px;
          line-height: 36px;
          letter-spacing: -0.02em;
          color: $text-default;
        }
      }
    }
  }
  @include mobile {
    .contents {
      display: flex;
      flex-direction: column;
      width: calc(100% - 48px);
      margin: 0 auto 0 auto;
      padding: 0 24px 0 24px;
    }
    .slogan {
      display: flex;
      flex-direction: column;
      align-items: center;
      width: 100%;
      height: 484px;
      background: $grey01;
      margin-bottom: 64px;
      .slogan-text {
        white-space: pre-wrap;
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        line-height: 24px;
        text-align: center;
        letter-spacing: -0.02em;

        color: $grey03;
      }
    }
    .title {
      font-style: normal;
      font-weight: bold;
      font-size: 32px;
      line-height: 48px;
      letter-spacing: -0.02em;
      white-space: pre-wrap;

      color: $black;
    }
    .info-table {
      .info-row {
        display: flex;
        flex-direction: column;
        margin-bottom: 64px;
        .title {
          padding-left: 24px;
        }
        .information {
          margin-top: 24px;
          overflow-x: auto;
          scrollbar-width: none;
          -ms-overflow-style: none;
          -webkit-overflow-scrolling: touch;
          &::-webkit-scrollbar {
            display: none;
          }
          display: flex;
          flex-direction: column;
          .cards {
            min-width: 752px;
            justify-content: space-between;
            display: inline-flex;
            flex: 0 0 auto;
            padding: 0 24px 0 24px;
          }
        }
      }
    }
    .activities {
      margin-bottom: 64px;
      display: flex;
      flex-direction: column;
      width: 100%;
      .desc {
        margin-top: 16px;
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        line-height: 24px;
        letter-spacing: -0.02em;
        white-space: pre-wrap;
        color: $text-default;
      }
      .cards {
        margin-top: 16px;
        display: flex;
        justify-content: space-between;
        flex-direction: column;
        // grid-gap: 16px;
        > div {
          margin-bottom: 16px;
        }
        > div:last-child {
          margin-bottom: 0;
        }
      }
    }
    .reviews {
      display: flex;
      flex-direction: column;
      .cards {
        margin-top: 16px;
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        justify-content: space-between;
        > div {
          margin-bottom: 16px;
        }
        > div:last-child {
          margin-bottom: 0;
        }
      }
      .more {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 72px;
        .lead-more {
          display: flex;
          justify-content: space-between;
          align-items: center;
          width: 106px;
          height: 40px;
          cursor: pointer;
          font-style: normal;
          font-weight: bold;
          font-size: 16px;
          line-height: 24px;
          letter-spacing: -0.02em;
          color: $text-default;
          img {
            width: 13.33px;
            height: 7.33px;
          }
        }
      }
    }
  }
}
</style>
