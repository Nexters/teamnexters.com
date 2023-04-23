<template>
  <transition name="recruitment" mode="out-in">
    <div>
      <Banner
        class="banner"
        :type="bannerType"
        :background-image-url="getBackgroundImage"
        :header-title="bannerTitle"
        :sub-title="bannerSubtitle"
        :period="bannerPeriod"
        :box-list="bannerBoxes"
        :remaining-period="remainingPeriod"
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
          :items="getQualifications"
        />
      </main>
      <main class="sub">
        <Schedule class="area schedule" :schedules="schedules" />
      </main>
      <main class="main third">
        <DotList :dot-list-title="`유의사항`" :items="getCautions" />
      </main>
      <div class="footer">
        <h2 class="footerTitle">궁금한 점이 있으신가요?</h2>
        <h3 class="footerSubTitle">자주 묻는 질문을 확인해보세요.</h3>
        <LinkButton
          :type="bannerType"
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
import background from "~/assets/css/r_export.scss";

export default defineComponent({
  name: "Recruitment",
  layout: "recruitment",
  transition: {
    name: "recruitment",
  },
  data() {
    return {
      banner: {
        bannerType: "DEFAULT",
        bannerTitle: "",
        bannerSubtitle: "",
        bannerPeriod: "",
        isVisible: false,
        remainingPeriod: -1,
        th: "",
        bannerBoxes: [],
      },
      notice: {
        isVisible: false,
        boxTitle: "",
        contents: [],
      },
      qualifications: [],
      schedules: [],
      cautions: [],
      recruitment_notice: "",
      recruitment_start: "",
      recruitment_end: "",
      ...background,
    };
  },
  async fetch() {
    const {
      th,
      is_visible_notice,
      notice_title,
      boxes,
      qualifications,
      schedules,
      cautions,
      notices,
      recruitment_start,
      recruitment_end,
    } = await this.$content("recruitment/recruitment")
      .only([
        "th",
        "is_visible_notice",
        "notice_title",
        "boxes",
        "qualifications",
        "schedules",
        "cautions",
        "notices",
        "recruitment_start",
        "recruitment_end",
      ])
      .fetch();
    const { recruitment_notice } = await this.$content("main")
      .only(["recruitment_notice"])
      .fetch();

    const bannerType = this.getType(
      recruitment_start,
      recruitment_end,
      recruitment_notice
    );

    this.banner.bannerType = bannerType;
    this.banner.th = th;
    this.banner.bannerTitle = this.makeBannerTitle(bannerType, th);
    this.banner.bannerSubtitle = this.makeBannerSubTitle(bannerType, th);
    this.banner.isVisible = this.isBannerDateVisible(bannerType);
    this.banner.bannerPeriod = this.banner.isVisible
      ? this.getDateWithDay(recruitment_start, recruitment_end)
      : "";
    this.banner.remainingPeriod =
      bannerType === "PROGRESS" ? this.getRemainingPeriod(recruitment_end) : -1;
    this.banner.bannerBoxes = boxes;
    this.notice.isVisible = is_visible_notice;
    this.notice.boxTitle = notice_title;
    this.notice.contents = notices.filter((notice) => notice.is_visible_notice);
    this.qualifications = qualifications.filter(
      (qualification) => qualification.is_visible_qualification
    );
    this.schedules = schedules;
    this.cautions = cautions.filter((caution) => caution.is_visible_caution);

    const yymmdd = (date) => {
      return new Date(new Date(date).setHours(0, 0, 0, 0));
    };
    this.recruitment_notice = yymmdd(recruitment_notice);
    this.recruitment_start = yymmdd(recruitment_start);
    this.recruitment_end = yymmdd(recruitment_end);
  },
  fetchOnServer: false,
  computed: {
    bannerType() {
      let type = "DEFAULT";
      if (this.before_recruitment) {
        type = "NOTICE";
      } else if (this.is_recruiting) {
        type = "PROGRESS";
      }
      return type;
    },
    bannerTitle() {
      return this.makeBannerTitle(this.bannerType, this.banner.th);
    },
    bannerSubtitle() {
      return this.makeBannerSubTitle(this.bannerType, this.banner.th);
    },
    bannerPeriod() {
      return this.is_recruiting
        ? this.getDateWithDay(this.recruitment_start, this.recruitment_end)
        : "";
    },
    remainingPeriod() {
      return this.getRemainingPeriod(this.recruitment_end);
    },
    bannerBoxes() {
      return this.banner.bannerBoxes.filter(
        (box) => box.type === this.bannerType
      );
    },
    getBackgroundImage() {
      let img = this.recruitment_default_desktop;
      if (this.bannerType === "NOTICE") {
        img = this.recruitment_notice_desktop;
      } else if (this.bannerType === "PROGRESS") {
        img = this.recruitment_wip_desktop;
      }
      return img;
    },
    getQualifications() {
      return this.qualifications.map((it) => ({
        id: it.id,
        text: it.qualification,
      }));
    },
    getCautions() {
      return this.cautions.map((it) => ({
        id: it.id,
        text: it.caution,
      }));
    },
    s_day() {
      const result = new Date(this.recruitment_start) - new Date();
      return Math.ceil(result / 86400000);
    },
    d_day() {
      const result = new Date(this.recruitment_end) - new Date();
      return this.s_day <= 0 ? Math.ceil(result / 86400000) : 0;
    },
    notice_day() {
      const result = new Date(this.recruitment_notice) - new Date();
      return Math.ceil(result / 86400000);
    },
    before_recruitment() {
      return this.notice_day <= 0 && this.s_day > 0;
    },
    is_recruiting() {
      return this.s_day <= 0 && this.d_day >= 0;
    },
  },
  methods: {
    makeBannerTitle(type, th) {
      switch (type) {
        case "DEFAULT": {
          return `NEXTERS\nRecruitment`;
        }
        case "NOTICE":
        case "PROGRESS": {
          return `NEXTERS ${th}${ th % 10 === 1? 'st': th % 10 === 2? 'nd': th % 10 === 3? 'rd': 'th' }\nRecruitment`;
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
    getType(startDate, endDate, noticeDate) {
      if (
        isNaN(Date.parse(startDate)) ||
        isNaN(Date.parse(endDate)) ||
        isNaN(Date.parse(noticeDate))
      ) {
        return "DEFAULT";
      }

      const now = new Date().getTime();
      const start = new Date(startDate).getTime();
      const end = new Date(endDate).getTime();
      const notice = new Date(noticeDate).getTime();

      if (now >= notice && now < start) {
        return "NOTICE";
      }
      if (this.is_recruiting) {
        return "PROGRESS";
      }

      return "DEFAULT";
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
