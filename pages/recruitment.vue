<template>
  <Fragment>
    <RecruitmentBanner
      :background-image-url="`https://drive.google.com/uc?export=view&id=1XyPcA3KsEO04sZ5pbdWVep3D6MmASEf7`"
      :header-title="`NEXTERS 20th\nRecruitment`"
      :sub-title="`곧 넥스터즈 20기 모집이 시작됩니다.`"
      :period="`2021. 5. 10(mon) ~6. 22(tue)`"
      :box-list="bannerBoxes"
    />
    <main class="main">
      <RecruitmentNoticeBox
        :box-title="notice.boxTitle"
        :contents="notice.contents"
      />
      <RecruitmentDotList
        class="area"
        :dot-list-title="`지원 자격`"
        :items="qualifications"
      />
      <RecruitmentSchedule class="area" :schedules="schedules" />
      <RecruitmentDotList
        class="area"
        :dot-list-title="`유의사항`"
        :items="caution"
      />
    </main>
    <div class="footer">
      <h2 class="footerTitle">궁금한 점이 있으신가요?</h2>
      <h3 class="footerSubTitle">자주 묻는 질문을 확인해보세요.</h3>
      <RecruitmentLinkButton
        class="faqBox"
        :buttonName="`FAQ 바로가기`"
        :link="`/contact`"
      />
    </div>
  </Fragment>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Recruitment",
  data() {
    return {
      bannerBoxes: [],
      notice: {
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
    this.bannerBoxes = result.bannerButtons;
    this.notice.boxTitle = result.banner[7];
    this.notice.contents = result.notice;
    this.qualifications = result.qualifications;
    this.schedules = result.schedules;
    this.caution = result.cautions;
  },
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
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
* {
  font-family: Spoqa Han Sans Neo;
}

.footer {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #f6f6f6;

  .footerTitle {
    font-weight: 700;
  }

  .footerSubTitle {
    font-weight: 400;
  }
}

@include desktop {
  .main {
    margin: 64px;
    max-width: 1200px;

    .area {
      margin-top: 120px;
    }
  }

  .footer {
    height: 323px;
    margin-top: 120px;

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
    margin: 64px;
    max-width: 1200px;

    .area {
      margin-top: 120px;
    }
  }

  .footer {
    height: 323px;
    margin-top: 120px;

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
    margin: 24px;
    max-width: 713px;

    .area {
      margin-top: 64px;
    }
  }

  .footer {
    height: 189px;
    margin-top: 64px;

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
