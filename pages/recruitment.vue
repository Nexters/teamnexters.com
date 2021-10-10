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
      bannerBoxes: [
        {
          id: 1,
          name: "모집 알람 신청하기",
          link: "www.naver.com",
        },
      ],
      notice: {
        boxTitle: "코로나 관련 사항을 꼭 참고해주세요!",
        contents: [
          {
            id: 1,
            text: "모집 및 활동은 코로나 19 전개 상황에 따라 중단 및 연기 될 수 있습니다.",
          },
          {
            id: 2,
            text: "사회적 거리두기, 방역수칙에 의거하여 활동합니다.",
          },
        ],
      },
      qualifications: [
        {
          id: 1,
          text: "학생 / 직장인 소속에 상관없이, 개발자 / 디자이너로 팀 프로젝트 수행이 가능한 분",
        },
        {
          id: 2,
          text: "실무에 가까운 협업과 창작하는 즐거움을 경험하고 싶으신 분",
        },
        {
          id: 3,
          text: "다양한 사람들과 폭넓고 깊이 있는 네트워킹을 원하시는 분",
        },
        {
          id: 4,
          text: "매주 토요일 오후 2시 ~6시에 진행되는 정규 활동에 성실하게 참여할 수 있으신 분\n(정규 활동은 방학동안 진행되며, 2회의 정규 활동을 이수하시면 수료로 인정됩니다.)",
        },
      ],
      schedules: [
        {
          id: 1,
          title: "서류 접수",
          date: "2021. 11. 26.",
        },
        {
          id: 2,
          title: "서류 합격 발표",
          date: "2021. 12. 05.",
        },
        {
          id: 3,
          title: "면접",
          date: "2021. 12. 09 ~ 10.",
        },
        {
          id: 4,
          title: "최종 합격 발표",
          date: "2021. 12. 28.",
        },
        {
          id: 5,
          title: "정규 활동",
          date: "2021. 12. ~ 2022.02",
        },
      ],
      caution: [
        {
          id: 1,
          text: "개발자 지원시, GitHub 계정을 필수로 제출해주셔야 합니다.",
        },
        {
          id: 2,
          text: "디자이너 지원시, 포트폴리오를 필수로 제출해주셔야 합니다.",
        },
        {
          id: 3,
          text: "지원서는 임시 저장이 불가합니다. 모든 문항을 채워주시고 제출해 주세요.",
        },
        {
          id: 4,
          text: "기재하신 개인정보는 NEXTERS 신입 회원 모집과 결과 전달을 위해 사용되며, 지원서 제출 시 개인정보 수집 및 이용에 동의한 것으로 간주합니다.\n다른 목적으로는 이용되지 않으며, 모집 기간 완료 즉시 폐기됩니다.",
        },
      ],
    };
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
