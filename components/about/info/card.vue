<template>
  <div class="info-container">
    <div class="contents">
      <h4 class="title">{{ title }}</h4>
      <h2 class="value">{{ value }}</h2>
      <p class="description">{{ description }}</p>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
const InfoCard = defineComponent({
  name: "InfoCard",
  props: {
    title: { type: String, required: true },
    value: { type: String, required: true },
    description: { type: String, required: true },
  },
});
export default InfoCard;
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";

* {
  font-family: Spoqa Han Sans Neo;
}
@include desktop {
  .info-container {
    border-radius: 16px;
    width: 378.67px;
    background: $grey01;
    .contents {
      padding: 32px;
      .title {
        font-size: 24px;
        line-height: 36px;
        font-weight: bold;
        margin-bottom: 8px;
        letter-spacing: -0.02em;
      }
      .value {
        font-style: normal;
        font-weight: bold;
        font-size: 48px;
        line-height: 64px;
        margin-bottom: 8px;
        letter-spacing: -0.02em;
      }
      .description {
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 27px;
        letter-spacing: -0.02em;

        color: $grey03;
      }
    }
  }
}
@include tablet {
  .info-container {
    flex: 0 0 auto;
    border-radius: 16px;
    width: 378.67px;
    background: $grey01;
    .contents {
      padding: 32px;
      .title {
        font-size: 24px;
        line-height: 36px;
        font-weight: bold;
        margin-bottom: 8px;
        letter-spacing: -0.02em;
      }
      .value {
        font-style: normal;
        font-weight: bold;
        font-size: 48px;
        line-height: 64px;
        margin-bottom: 8px;
        letter-spacing: -0.02em;
      }
      .description {
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 27px;
        letter-spacing: -0.02em;

        color: $grey03;
      }
    }
  }
}
@include mobile {
  .info-container {
    flex: 0 0 auto;
    border-radius: 8px;
    width: 240px;
    background: $grey01;
    .contents {
      padding: 24px;
      .title {
        font-size: 16px;
        line-height: 24px;
        font-weight: bold;
        margin-bottom: 4px;
        letter-spacing: -0.02em;
      }
      .value {
        font-style: normal;
        font-weight: bold;
        font-size: 32px;
        line-height: 48px;
        margin-bottom: 4px;
        letter-spacing: -0.02em;
      }
      .description {
        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 21px;
        letter-spacing: -0.02em;

        color: $grey03;
      }
    }
  }
}
</style>
