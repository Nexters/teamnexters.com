<template>
  <div class="container">
    <div class="slogan">
      <p class="title">IT Community</p>
      <p class="title">for Experts</p>
      <p class="description">개발자와 디자이너를 위한 IT 커뮤니티입니다.</p>
      <div class="quick-link">
        <p>넥스터즈 알아보기</p>
        <img src="~/assets/img/ic_forward.png" />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Main",
  layout: "main",
  setup() {
    return {};
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";

.container {
  width: 100%;
  color: #ffffff;
  display: flex;
  margin: auto;
  .quick-link {
    display: flex;
    flex-direction: row;
    align-content: center;
    padding-top: 40px;

    font-style: normal;
    font-weight: bold;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: -0.02em;

    cursor: pointer;

    img {
      width: 16px;
      height: 16px;
      margin: auto 0 auto 8px;
    }
  }
  @include mobile {
    .slogan {
      width: 327px;
      height: 208px;
      padding: 24px;
      .title {
        font-style: normal;
        font-weight: 900;
        font-size: 40px;
        line-height: 47.73px;
      }
      .description {
        margin-top: 16px;
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        line-height: 24px;
        letter-spacing: -0.02em;
      }
    }
  }
  @include tablet {
    .slogan {
      width: 327px;
      height: 208px;
      padding: 24px;
      .title {
        font-style: normal;
        font-weight: 900;
        font-size: 40px;
        line-height: 47.73px;
      }
      .description {
        margin-top: 16px;
        font-style: normal;
        font-weight: normal;
        font-size: 16px;
        line-height: 24px;
        letter-spacing: -0.02em;
      }
    }
  }
  @include desktop {
    .slogan {
      width: 1200px;
      height: 438px;
      margin: auto;
      padding: 64px;
      .title {
        font-style: normal;
        font-weight: 900;
        font-size: 100px;
        line-height: 119px;
      }
      .description {
        margin-top: 32px;
        font-style: normal;
        font-weight: normal;
        font-size: 24px;
        line-height: 36px;
        letter-spacing: -0.02em;
      }
    }
  }
}
</style>
