<template>
  <section class="scheduleBox">
    <h2 class="scheduleTitle">{{ scheduleTitle }}</h2>
    <p class="schedule">{{ scheduleDate }}</p>
  </section>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "ScheduleBox",
  props: {
    scheduleTitle: {
      type: String,
      require: true,
    },
    scheduleDate: {
      type: String,
      require: true,
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

.scheduleBox {
  display: flex;
  justify-content: center;
  background: $background-sub;

  .scheduleTitle {
    font-weight: bold;
  }

  .schedule {
    font-weight: 400;
  }
}

@include desktop {
  .scheduleBox {
    min-width: 200px;
    flex-direction: column;
    padding: 24px;
    border-radius: 16px;

    .scheduleTitle {
      font-size: 24px;
      line-height: 36px;
    }

    .schedule {
      font-size: 18px;
      line-height: 27px;
    }
  }
}

@include tablet {
  .scheduleBox {
    min-width: 200px;
    flex-direction: column;
    padding: 24px;
    border-radius: 16px;

    .scheduleTitle {
      font-size: 24px;
      line-height: 36px;
    }

    .schedule {
      font-size: 18px;
      line-height: 27px;
    }
  }
}

@include mobile {
  .scheduleBox {
    min-width: 100%;
    justify-content: space-between;
    padding: 16px;
    border-radius: 8px;

    .scheduleTitle {
      font-size: 16px;
      line-height: 24px;
    }

    .schedule {
      font-size: 14px;
      line-height: 21px;
    }
  }
}
</style>
