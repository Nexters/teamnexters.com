<template>
  <div class="error-background">
    <div class="error-area">
      <div class="error-text">
        <img class="ic-caution" src="~/assets/img/ic_caution.svg" />
        <h2>Sorry</h2>
        <h4 v-if="error.statusCode === 404">This page could not found</h4>
        <h4 v-else>An error occurred</h4>
      </div>
      <div class="primary-button">
        <nuxt-link to="/">Back to Home</nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["error"],
};
</script>
<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";
@import "~/assets/css/main-bg.scss";

.error-area {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.error-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.primary-button {
  margin-top: 32px;
  background-color: $background-primary;
  > a {
    text-decoration: none;
    color: white;
  }
}
.error-text {
  > h2 {
    margin-bottom: 8px;
    font-weight: bold;
    letter-spacing: -0.02em;
  }
  > h4 {
    font-weight: normal;
    letter-spacing: -0.02em;
  }
}

@include desktop {
  .ic-caution {
    width: 66.67px;
    height: 66.67px;
  }
  .error-area {
    width: 1200px;
  }
  .error-text {
    > h2 {
      font-size: 48px;
      line-height: 64px;
      margin-top: 14.67px;
    }
    > h4 {
      font-size: 24px;
      line-height: 36px;
    }
  }

  .primary-button {
    padding: 24px 40px;
    border-radius: 8px;
  }
}
@include tablet {
  .ic-caution {
    width: 33.33px;
    height: 33.33px;
  }
  .error-area {
    width: 327px;
  }
  .error-text {
    > h2 {
      font-size: 32px;
      line-height: 48px;
      margin-top: 11.33px;
    }
    > h4 {
      font-size: 16px;
      line-height: 24px;
    }
  }
  .primary-button {
    padding: 16px 24px;
    border-radius: 4px;
  }
}
@include mobile {
  .ic-caution {
    width: 33.33px;
    height: 33.33px;
  }
  .error-area {
    width: 327px;
  }
  .error-text {
    > h2 {
      font-size: 32px;
      line-height: 48px;
      margin-top: 11.33px;
    }
    > h4 {
      font-size: 16px;
      line-height: 24px;
    }
  }
  .primary-button {
    padding: 16px 24px;
    border-radius: 4px;
  }
}
</style>
