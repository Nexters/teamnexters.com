<template>
  <div class="activity-container" :style="`background: ${thumbnail}`">
    <div class="contents">
      <p class="description">{{ description }}</p>
      <p class="title">{{ title }}</p>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
const ActivityCard = defineComponent({
  name: "ActivityCard",
  props: {
    description: { type: String, required: true },
    title: { type: String, required: true },
    thumbnail: { type: String, required: true },
  },
});
export default ActivityCard;
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
* {
  font-family: Spoqa Han Sans Neo;
}

@import "~/assets/css/setting.scss";

@include desktop {
  .activity-container {
    border-radius: 16px;
    width: 576px;
    height: 324px;
    background: rgba(0, 0, 0, 0.5);
    .contents {
      padding: 32px;
      display: flex;
      flex-direction: column;
      height: calc(100% - 64px);
      .description {
        white-space: pre-wrap;
        font-style: normal;
        font-weight: bold;
        font-size: 32px;
        line-height: 48px;
        letter-spacing: -0.02em;

        color: $white;
      }
      .title {
        margin-top: auto;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 27px;
        letter-spacing: -0.02em;

        color: $white;
      }
    }
  }
}
@include tablet {
  .activity-container {
    border-radius: 16px;
    width: calc(50% - 16px);
    height: 324px;
    background: rgba(0, 0, 0, 0.5);
    .contents {
      padding: 32px;
      display: flex;
      flex-direction: column;
      height: calc(100% - 64px);
      .description {
        white-space: pre-wrap;
        font-style: normal;
        font-weight: bold;
        font-size: 32px;
        line-height: 48px;
        letter-spacing: -0.02em;

        color: $white;
      }
      .title {
        margin-top: auto;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 27px;
        letter-spacing: -0.02em;
        color: $white;
      }
    }
  }
}
@include mobile {
  .activity-container {
    border-radius: 8px;
    width: 100%;
    height: 184px;
    background: rgba(0, 0, 0, 0.5);
    .contents {
      padding: 24px;
      display: flex;
      flex-direction: column;
      height: calc(100% - 48px);
      .description {
        white-space: pre-wrap;
        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 36px;
        letter-spacing: -0.02em;

        color: $white;
      }
      .title {
        margin-top: auto;
        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 21px;
        letter-spacing: -0.02em;
        color: $white;
      }
    }
  }
}
</style>
