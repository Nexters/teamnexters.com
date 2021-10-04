<template>
  <div class="container">
    <div class="slogan">
      <h1 class="slogan-text">{{ slogan }}</h1>
    </div>
    <div class="contents">
      <!-- horizontal scroll -->
      <div class="information">
        <h2 class="title">{{ info.title }}</h2>
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

      <div class="activities">
        <ActivityCard
          v-for="item in act.items"
          :key="item.title"
          :title="item.title"
          :value="item.value"
          :description="item.description"
        />
      </div>
      <div class="reviews"></div>
      <div>Lead more</div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "AboutPage",
  layout: "DefaultLayout",
  async asyncData({ $content }) {
    const informations = await $content("about/informations")
      .only(["title", "value", "description"])
      .fetch();
    return { info: { title: "10년째\n멈추지 않는 열정", items: informations } };
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
        items: [],
      },
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
  animation: fadein 3s;
  -moz-animation: fadein 3s; /* Firefox */
  -webkit-animation: fadein 3s; /* Safari and Chrome */
  -o-animation: fadein 3s; /* Opera */
}
@include desktop {
  .contents {
    width: 1200px;
    margin: 0 auto 0 auto;
  }
  .slogan {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 64px;
    width: 100%;
    height: 809px;
    background: #f6f6f6;
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

      color: #777777;
    }
  }
  .title {
    font-style: normal;
    font-weight: bold;
    font-size: 60px;
    line-height: 90px;
    letter-spacing: -0.02em;
    white-space: pre-wrap;

    color: #000000;
  }
  .information {
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
</style>
