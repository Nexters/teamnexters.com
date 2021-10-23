<template>
  <div class="review-container" @click="onClick">
    <div class="contents">
      <p class="title">{{ title }}</p>
      <p class="author">{{ th }} | {{ author }}</p>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
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
@import "~/assets/css/color.scss";

* {
  font-family: Spoqa Han Sans Neo;
}
@include desktop {
  .review-container {
    cursor: pointer;
    border-radius: 16px;
    width: 378.67px;
    height: 163px;
    background: $grey01;
    .contents {
      padding: 24px;
      display: flex;
      flex-direction: column;
      .title {
        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 36px;
        letter-spacing: -0.02em;

        color: $black;
      }
      .author {
        margin-top: 16px;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 27px;
        letter-spacing: -0.02em;
        color: $text-default;
      }
    }
  }
}
@include tablet {
  .review-container {
    cursor: pointer;
    border-radius: 16px;
    width: calc(50% - 16px);
    height: 163px;
    background: $grey01;
    .contents {
      padding: 24px;
      height: calc(100% - 48px);
      display: flex;
      flex-direction: column;
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

        color: $black;
      }
      .author {
        margin-top: 16px;
        font-style: normal;
        font-weight: normal;
        font-size: 18px;
        line-height: 27px;
        letter-spacing: -0.02em;
        color: $text-default;
      }
    }
  }
}
@include mobile {
  .review-container {
    cursor: pointer;
    border-radius: 8px;
    width: 100%;
    background: $grey01;
    .contents {
      padding: 24px;
      display: flex;
      flex-direction: column;
      .title {
        width: 100%;

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

        color: $black;
      }
      .author {
        margin-top: 8px;
        font-style: normal;
        font-weight: normal;
        font-size: 14px;
        line-height: 21px;
        letter-spacing: -0.02em;
        color: $text-default;
      }
    }
  }
}
</style>
