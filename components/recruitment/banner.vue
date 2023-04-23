<template>
  <div
    class="banner"
    :class="type"
    :style="{ 'background-image': backgroundImageUrl }"
  >
    <div class="bannerMetaWrap">
      <h1 class="bannerTitle">{{ headerTitle }}</h1>
      <h2 class="bannerSubTitle">{{ subTitle }}</h2>
      <p v-if="isVisibleDate" class="bannerPeriod">
        <span>{{ period }}</span>
        <Badge v-if="remainingPeriod >= 0" class="badge" :text="badgeText" />
      </p>
      <article class="boxArea">
        <LinkButton
          v-for="box in boxList"
          :key="box.id"
          :type="type"
          class="box"
          :button-name="box.name"
          :href="`${box.link}`"
        />
      </article>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Banner",
  props: {
    type: {
      type: String,
      require: true,
    },
    backgroundImageUrl: {
      type: String,
      require: true,
    },
    headerTitle: {
      type: String,
      require: true,
    },
    subTitle: {
      type: String,
      require: true,
    },
    period: {
      type: String,
      require: false,
    },
    boxList: {
      type: Array,
      require: false,
    },
    remainingPeriod: {
      type: Number,
      require: false,
    },
  },
  computed: {
    isVisibleDate() {
      return this.type !== "DEFAULT";
    },
    badgeText() {
      return this.remainingPeriod > 0
        ? `마감 D-${this.remainingPeriod}`
        : "마감 D-day";
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";

* {
  font-family: Spoqa Han Sans Neo;
}

.banner {
  width: 100%;
  height: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  box-sizing: border-box;
  letter-spacing: -0.02em;

  .bannerTitle {
    color: $text-default;
    font-weight: 800;
    white-space: pre-wrap;
    font-family: "Montserrat", sans-serif;
  }

  .bannerSubTitle {
    font-weight: 400;
    color: $text-default;
    white-space: pre-wrap;
  }

  .bannerPeriod {
    display: flex;
    font-weight: 700;
    color: $text-default;
    align-items: center;
  }

  &.PROGRESS {
    .bannerTitle {
      color: $text-inverse;
    }

    .bannerSubTitle {
      color: $text-inverse;
    }

    .bannerPeriod {
      color: $text-inverse;
    }
  }

  &.NOTICE {
    .bannerTitle {
      color: $text-inverse;
    }

    .bannerSubTitle {
      color: $text-inverse;
    }

    .bannerPeriod {
      color: $text-inverse;
    }
  }

  .boxArea {
    .box {
      margin-right: 10px;
    }
  }
}

@include desktop {
  .banner {
    height: 610px;
    padding-left: 64px;
    padding-right: 64px;

    .bannerMetaWrap {
      width: 1200px;
      margin: auto;
    }

    .bannerTitle {
      font-size: 60px;
      line-height: 73px;
      font-family: "Montserrat", sans-serif;
    }

    .bannerSubTitle {
      font-size: 24px;
      line-height: 36px;
      margin-top: 16px;
    }

    .bannerPeriod {
      font-size: 24px;
      line-height: 36px;
      margin-top: 16px;

      .badge {
        margin-left: 16px;
      }
    }

    .boxArea {
      margin-top: 32px;

      .box {
        height: 84px;
      }
    }
  }
}

@include tablet {
  .banner {
    height: 610px;
    padding-left: 64px;
    padding-right: 64px;

    .bannerMetaWrap {
      width: 100%;
      margin: auto;
    }

    .bannerTitle {
      font-size: 60px;
      line-height: 73px;
      font-family: "Montserrat", sans-serif;
    }

    .bannerSubTitle {
      font-size: 24px;
      line-height: 36px;
      margin-top: 16px;
    }

    .bannerPeriod {
      font-size: 24px;
      line-height: 36px;
      margin-top: 16px;

      .badge {
        margin-left: 16px;
      }
    }

    .boxArea {
      margin-top: 32px;

      .box {
        height: 84px;
      }
    }
  }
}

@include mobile {
  .banner {
    height: 354px;
    padding-left: 24px;
    padding-right: 24px;

    .bannerMetaWrap {
      width: 713px;
      max-width: 713px;
      margin: auto;
    }

    .bannerTitle {
      font-size: 32px;
      line-height: 38px;
      font-family: "Montserrat", sans-serif;
    }

    .bannerSubTitle {
      font-size: 16px;
      line-height: 24px;
      margin-top: 8px;
    }

    .bannerPeriod {
      font-size: 16px;
      line-height: 24px;
      margin-top: 8px;

      .badge {
        margin-left: 8px;
      }
    }

    .boxArea {
      margin-top: 16px;

      .box {
        height: 56px;
      }
    }
  }
}
</style>
