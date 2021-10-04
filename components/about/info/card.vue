<template>
  <div class="info-container">
    <div class="contents">
      <p class="title">{{ title }}</p>
      <p class="value">{{ value }}</p>
      <p class="description">{{ description }}</p>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";
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
* {
  font-family: Spoqa Han Sans Neo;
}
@include desktop {
  .info-container {
    border-radius: 16px;
    width: 368px;
    height: 233px;
    background: #f6f6f6;
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
        font-size: 60px;
        line-height: 90px;
        margin-bottom: 8px;
        letter-spacing: -0.02em;
      }
      .description {
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 27px;
        letter-spacing: -0.02em;

        color: #777777;
      }
    }
  }
}
@include tablet {
  .info-container {
    flex: 0 0 auto;
    border-radius: 16px;
    width: 368px;
    height: 233px;
    background: #f6f6f6;
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
        font-size: 60px;
        line-height: 90px;
        margin-bottom: 8px;
        letter-spacing: -0.02em;
      }
      .description {
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 27px;
        letter-spacing: -0.02em;

        color: #777777;
      }
    }
  }
}
@include mobile {
  .info-container {
    flex: 0 0 auto;
    border-radius: 16px;
    width: 240px;
    height: 149px;
    background: #f6f6f6;
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

        color: #777777;
      }
    }
  }
}
</style>
