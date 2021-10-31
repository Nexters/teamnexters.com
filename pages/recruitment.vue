<template>
  <transition name="recruitment" mode="out-in">
    <div>
      <Banner
        class="banner"
        :type="banner.bannerType"
        :background-image-url="`https://drive.google.com/uc?export=view&id=${banner.bannerImage}`"
        :header-title="banner.bannerTitle"
        :sub-title="banner.bannerSubtitle"
        :period="banner.bannerPeriod"
        :box-list="bannerBoxes"
        :remaining-period="banner.remainingPeriod"
      />
      <main class="main">
        <NoticeBox
          v-if="notice.isVisible"
          :box-title="notice.boxTitle"
          :contents="notice.contents"
        />
        <DotList
          class="area"
          :dot-list-title="`지원 자격`"
          :items="qualifications"
        />
      </main>
      <main class="sub">
        <Schedule class="area schedule" :schedules="schedules" />
      </main>
      <main class="main third">
        <DotList :dot-list-title="`유의사항`" :items="caution" />
      </main>
      <div class="footer">
        <h2 class="footerTitle">궁금한 점이 있으신가요?</h2>
        <h3 class="footerSubTitle">자주 묻는 질문을 확인해보세요.</h3>
        <LinkButton
          :type="banner.bannerType"
          class="faqBox"
          :button-name="`FAQ 바로가기`"
          :href="`/contact#faq`"
        />
      </div>
    </div>
  </transition>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Recruitment",
  transition: {
    name: "recruitment",
  },
  data() {
    return {
      banner: {
        bannerType: "DEFAULT",
        bannerTitle: "",
        bannerSubtitle: "",
        bannerImage: "",
        bannerPeriod: "",
        isVisible: false,
        remainingPeriod: -1,
      },
      bannerBoxes: [],
      notice: {
        isVisible: false,
        boxTitle: "",
        contents: [],
      },
      qualifications: [],
      schedules: [],
      caution: [],
    };
  },
  async fetch() {
    const result = await this.FetchAll();
    const bannerType = result.banner[6];
    this.banner.bannerType = bannerType;
    this.banner.bannerImage = result.banner[0];
    this.banner.bannerTitle = this.makeBannerTitle(
      bannerType,
      result.banner[1]
    );
    this.banner.bannerSubtitle = this.makeBannerSubTitle(
      bannerType,
      result.banner[1]
    );
    this.banner.isVisible = this.isBannerDateVisible(bannerType);
    this.banner.bannerPeriod = this.banner.isVisible
      ? this.getDateWithDay(result.banner[2], result.banner[3])
      : "";
    this.banner.remainingPeriod =
      bannerType === "PROGRESS"
        ? this.getRemainingPeriod(result.banner[3])
        : -1;
    this.bannerBoxes = result.bannerButtons;
    this.notice.isVisible = result.banner[4] === "TRUE";
    this.notice.boxTitle = result.banner[5];
    this.notice.contents = result.notice;
    this.qualifications = result.qualifications;
    this.schedules = result.schedules;
    this.caution = result.cautions;
  },
  fetchOnServer: false,
  methods: {
    debug(e) {
      console.log(e);
    },
    FetchAll: async function () {
      const { results } = await this.$content("recruitment").fetch();

      const { rawData: banner } = results[0].result;
      const { rawData: buttons } = results[1].result;
      const { rawData: qualifications } = results[2].result;
      const { rawData: schedules } = results[3].result;
      const { rawData: cautions } = results[4].result;
      const { rawData: notices } = results[5].result;

      const [_, ...recruitmentBanner] = banner;
      const [__, ...recruitmentButtons] = buttons;
      const [___, ...recruitmentQualifications] = qualifications;
      const [____, ...recruitmentSchedules] = schedules;
      const [_____, ...recruitmentCautions] = cautions;
      const [______, ...recruitmentNotices] = notices;

      const result = {
        banner: recruitmentBanner[0],
        bannerButtons: recruitmentButtons
          .filter((it) => it[2] === "TRUE")
          .map((it, idx) => ({
            id: idx,
            name: it[0],
            link: it[1],
          })),
        qualifications: recruitmentQualifications
          .filter((it) => it[1] === "TRUE")
          .map((it, idx) => ({
            id: idx,
            text: it[0],
          })),
        schedules: recruitmentSchedules.map((it, idx) => ({
          id: idx,
          title: it[0],
          date: it[1],
        })),
        cautions: recruitmentCautions
          .filter((it) => it[1] === "TRUE")
          .map((it, idx) => ({
            id: idx,
            text: it[0],
          })),
        notice: recruitmentNotices
          .filter((it) => it[1] === "TRUE")
          .map((it, idx) => ({
            id: idx,
            text: it[0],
          })),
      };

      return result;
    },
    makeBannerTitle(type, th) {
      switch (type) {
        case "DEFAULT": {
          return `NEXTERS\nRecruitment`;
        }
        case "NOTICE":
        case "PROGRESS": {
          return `NEXTERS ${th}th\nRecruitment`;
        }
      }
      return "";
    },
    makeBannerSubTitle(type, th) {
      switch (type) {
        case "DEFAULT": {
          return `현재 모집기간이 아닙니다.\n모집이 시작되면 메일을 보내드립니다.`;
        }
        case "NOTICE": {
          return `곧 넥스터즈 ${th}기 모집이 시작됩니다.`;
        }
        case "PROGRESS": {
          return `넥스터즈 ${th}기 모집 중입니다.`;
        }
      }
      return "";
    },
    isBannerDateVisible(type) {
      return type !== "DEFAULT";
    },
    getDateWithDay(startDate, endDate) {
      const days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"];
      const sd = new Date(startDate);
      const ed = new Date(endDate);
      const year = sd.getFullYear();
      const sdMonth = sd.getMonth() + 1;
      const sdDate = sd.getDate();
      const sdDay = days[sd.getDay()];
      const start = `${year}. ${sdMonth}. ${sdDate}(${sdDay})`;
      let end = "";

      if (!isNaN(Date.parse(ed))) {
        const edMonth = ed.getMonth() + 1;
        const edDate = ed.getDate();
        const edDay = days[ed.getDay()];
        end = `${edMonth}. ${edDate}(${edDay})`;
      }

      return `${start} ~ ${end}`;
    },
    getRemainingPeriod(endDate) {
      const ed = new Date(endDate);

      if (isNaN(Date.parse(ed))) {
        return -1;
      }

      const now = new Date();
      return Math.ceil((ed.getTime() - now.getTime()) / (1000 * 3600 * 24));
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
  display: flex;
  justify-content: center;
  align-items: center;
  padding-top: 84px;
  padding-bottom: 48px;
}

.recruitment-enter-active,
.recruitment-leave-active {
  transition: opacity 1.5s;
}
.recruitment-enter,
.recruitment-leave-active {
  opacity: 0;
}

.main {
  margin: auto;
}

.sub {
  margin: auto;
}

.footer {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: $background-sub;

  .footerTitle {
    font-weight: 700;
  }

  .footerSubTitle {
    font-weight: 400;
  }
}

@include desktop {
  .main {
    padding: 64px 64px 0;
    max-width: 1200px;

    .area {
      margin-top: 120px;
    }

    &.third {
      padding-top: 120px;
    }
  }

  .sub {
    padding: 64px;
    max-width: 1200px;
    margin-top: 120px;
  }

  .footer {
    height: 323px;
    margin-top: 120px;
    margin-bottom: 64px;

    .footerTitle {
      font-size: 24px;
      line-height: 36px;
    }

    .footerSubTitle {
      font-size: 18px;
      line-height: 27px;
      margin-top: 16px;
    }

    .faqBox {
      margin-top: 32px;
    }
  }
}

@include tablet {
  .main {
    padding: 64px 64px 0;
    max-width: 1200px;

    .area {
      margin-top: 120px;
    }

    &.third {
      padding-top: 120px;
    }
  }

  .sub {
    padding-left: 0;
    max-width: 1200px;
    margin-top: 120px;
  }

  .footer {
    height: 323px;
    margin-top: 120px;
    margin-bottom: 64px;

    .footerTitle {
      font-size: 24px;
      line-height: 36px;
    }

    .footerSubTitle {
      font-size: 18px;
      line-height: 27px;
      margin-top: 16px;
    }

    .faqBox {
      margin-top: 32px;
    }
  }
}

@include mobile {
  .main {
    padding: 24px 24px 0;
    max-width: 713px;

    .area {
      margin-top: 64px;
    }

    &.third {
      padding-top: 64px;
    }
  }

  .sub {
    padding: 24px 24px 0;
    max-width: 713px;
    margin-top: 64px;
  }

  .footer {
    height: 189px;
    margin-top: 64px;
    margin-bottom: 24px;

    .footerTitle {
      font-size: 16px;
      line-height: 24px;
    }

    .footerSubTitle {
      font-size: 14px;
      line-height: 21px;
      margin-top: 8px;
    }

    .faqBox {
      margin-top: 16px;
    }
  }
}
</style>
