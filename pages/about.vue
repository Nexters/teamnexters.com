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
            <div class="more">
              <div class="lead-more">
                <p>Lead more</p>
                <img src="~/assets/img/ic_down.png" alt="" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script lang="ts">
import { defineComponent } from "@nuxtjs/composition-api";

export default defineComponent({
  name: "AboutPage",
  transition: {
    name: "about",
  },
  async asyncData({ $content }) {
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
      .fetch();
    return {
      info: { title: "10년째\n멈추지 않는 열정", items: informations },
      act: { title: "함께하는\n다양한 활동", items: activities },
      review: { title: "회원들의\n생생한 활동 후기", items: reviews },
    };
  },
  data() {
    return {
      slogan:
        "NEXTERS는 IT업계를 주도하는\n개발자와 디자이너를 위한 모임입니다.\n\n자유롭게 협업하고 소통하며,\n자기역량 강화, 새로운 서비스 경험을 통해\nIT 인재가 되는 것을 목표로 합니다.\n\n수도권 중심으로 대학생과 직장인이 활동하며,\n대학생은 실무에 준하는 경험을,\n직장인은 새로운 도전을 경험할 수 있습니다.",
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
      },
    };
  },
  fetchOnServer: false,
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";

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
  box-sizing: border-box;
  h1 {
    &::before {
      display: block;
      content: "";
      height: 73px;
    }
  }
}

.about-container {
  @include desktop {
    .contents {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 64px;
      width: 100%;
      margin: 0 auto 0 auto;
    }
    .slogan {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding-top: 64px;
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
        /* or 150% */

        text-align: center;
        letter-spacing: -0.02em;

        /* text/sub */

        color: $grey03;
      }
    }
    .title {
      font-style: normal;
      font-weight: bold;
      font-size: 60px;
      line-height: 90px;
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
        gap: 48px;
        .cards {
          display: flex;
          justify-content: center;
          gap: 48px;
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
      gap: 48px;
      .cards {
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        gap: 48px;
      }
    }
    .review-row {
      display: flex;
      justify-content: center;
      margin-bottom: 120px;
    }
    .reviews {
      display: flex;
      flex-direction: column;
      width: 1200px;
      gap: 24px;
      .cards {
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        gap: 24px;
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
          color: $grey03;
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
      padding-top: 64px;
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
        /* or 150% */

        text-align: center;
        letter-spacing: -0.02em;

        /* text/sub */

        color: $grey03;
      }
    }
    .title {
      font-style: normal;
      font-weight: bold;
      font-size: 60px;
      line-height: 90px;
      letter-spacing: -0.02em;
      white-space: pre-wrap;

      color: $black;
    }
    .info-table {
      padding-left: 64px;
      .info-row {
        display: flex;
        flex-direction: column;
        margin-bottom: 120px;
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
            gap: 48px;
            display: flex;
            flex: 0 0 auto;
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
      gap: 48px;
      .cards {
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        gap: 48px;
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
      gap: 24px;
      .cards {
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        gap: 24px;
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
          color: $grey03;
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
      padding-top: 24px;
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
      padding-left: 24px;
      .info-row {
        display: flex;
        flex-direction: column;
        margin-bottom: 64px;
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
            gap: 48px;
            display: flex;
            flex: 0 0 auto;
          }
        }
      }
    }
    .activities {
      margin-bottom: 64px;
      display: flex;
      flex-direction: column;
      width: 100%;
      gap: 24px;
      .cards {
        display: flex;
        flex-direction: column;
        gap: 24px;
      }
    }
    .reviews {
      display: flex;
      flex-direction: column;
      gap: 24px;
      .cards {
        display: flex;
        flex-direction: row;
        box-sizing: border-box;
        flex-wrap: wrap;
        gap: 16px;
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
          color: $grey03;
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
