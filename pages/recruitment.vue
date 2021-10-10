<template>
  <RecruitmentBanner
    :background-image-url="`https://drive.google.com/uc?export=view&id=1XyPcA3KsEO04sZ5pbdWVep3D6MmASEf7`"
    :header-title="`NEXTERS 20th\nRecruitment`"
    :sub-title="`곧 넥스터즈 20기 모집이 시작됩니다.`"
    :period="`2021. 5. 10(mon) ~6. 22(tue)`"
    :boxList="boxs"
  />
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Recruitment",
  data() {
    return {
      boxs: [
        {
          id: 1,
          name: "모집 알람 신청하기",
          link: "www.naver.com",
        },
      ],
    };
  },
});
</script>

<style scoped></style>
