<template>
  <div
    class="banner"
    :style="{ 'background-image': 'url(' + backgroundImageUrl + ')' }"
  >
    <h1 class="bannerTitle">{{ headerTitle }}</h1>
    <h2 class="bannerSubTitle">{{ subTitle }}</h2>
    <p class="bannerPeriod">{{ period }}</p>
    <article class="boxArea">
      <RecruitmentLinkButton
        v-for="box in boxList"
        :key="box.id"
        class="box"
        :button-name="box.name"
        :link="box.link"
      />
    </article>
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Banner",
  props: {
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
  box-sizing: border-box;

  .bannerTitle {
    color: $white;
    font-weight: 900;
    white-space: pre-wrap;
  }

  .bannerSubTitle {
    font-weight: 400;
    color: $white;
    white-space: pre-wrap;
  }

  .bannerPeriod {
    font-weight: 700;
    color: $white;
  }

  .boxArea {
    .box {
      margin-right: 10px;
    }
  }
}

@include desktop {
  .banner {
    height: 624px;
    padding: 64px;

    .bannerTitle {
      font-size: 60px;
      line-height: 72px;
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
    height: 624px;
    padding: 64px;

    .bannerTitle {
      font-size: 60px;
      line-height: 72px;
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
    height: 376px;
    padding: 24px;

    .bannerTitle {
      font-size: 32px;
      line-height: 38px;
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
