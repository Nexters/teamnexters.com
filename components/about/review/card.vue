<template>
  <div class="review-container" @click="onClick">
    <div class="contents">
      <p
        class="th"
        :style="`background: ${thBackgroundColor}; color:${thTextColor}`"
      >
        {{ th }}
      </p>
      <p class="title">{{ title }}</p>
      <p class="author">{{ author }}</p>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";
const ReviewCard = defineComponent({
  name: "ReviewCard",
  props: {
    th: { type: String, required: true },
    thBackgroundColor: { type: String, required: true },
    thTextColor: { type: String, required: true },
    title: { type: String, required: true },
    author: { type: String, required: true },
    href: { type: String, required: true },
  },
  methods: {
    onClick: function () {
      window.location.href = this.href;
    },
  },
});
export default ReviewCard;
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
* {
  font-family: Spoqa Han Sans Neo;
}
@include desktop {
  .review-container {
    cursor: pointer;
    border-radius: 16px;
    width: 384px;
    height: 192px;
    background: #f6f6f6;
    .contents {
      padding: 24px;
      height: calc(100% - 48px);
      display: flex;
      flex-direction: column;
      .th {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 49px;
        height: 29px;
        border-radius: 4px;

        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 21px;
        /* identical to box height, or 150% */

        letter-spacing: -0.02em;

        color: #5236ff;
      }
      .title {
        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 36px;
        letter-spacing: -0.02em;

        color: #000000;
      }
      .author {
        margin-top: auto;
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
  .review-container {
    cursor: pointer;
    border-radius: 16px;
    width: calc(50% - 12px);
    height: 192px;
    background: #f6f6f6;
    .contents {
      padding: 24px;
      height: calc(100% - 48px);
      display: flex;
      flex-direction: column;
      .th {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 49px;
        height: 29px;
        border-radius: 4px;

        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 21px;
        /* identical to box height, or 150% */

        letter-spacing: -0.02em;

        color: #5236ff;
      }
      .title {
        width: 296.5px;
        height: 72px;

        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;

        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 36px;
        letter-spacing: -0.02em;

        color: #000000;
      }
      .author {
        margin-top: auto;
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
  .review-container {
    cursor: pointer;
    border-radius: 8px;
    width: 100%;
    height: 149px;
    background: #f6f6f6;
    .contents {
      padding: 24px;
      height: calc(100% - 48px);
      display: flex;
      flex-direction: column;
      .th {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 41px;
        height: 24px;
        border-radius: 4px;

        font-style: normal;
        font-weight: normal;
        font-size: 12px;
        line-height: 18px;

        letter-spacing: -0.02em;

        color: #5236ff;
      }
      .title {
        width: 100%;
        height: 48px;

        overflow: hidden;
        text-overflow: ellipsis;
        display: -webkit-box;
        -webkit-line-clamp: 2;
        -webkit-box-orient: vertical;

        font-style: normal;
        font-weight: bold;
        font-size: 16px;
        line-height: 24px;
        letter-spacing: -0.02em;

        color: #000000;
      }
      .author {
        margin-top: auto;
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
