<template>
  <div class="scheduleArea">
    <h2 class="scheduleTitle">모집 일정</h2>
    <article class="schedules">
      <ScheduleBox
        v-for="schedule in schedules"
        :key="schedule.id"
        class="schedule"
        :schedule-title="schedule.title"
        :schedule-date="schedule.date"
      />
    </article>
  </div>
</template>

<script>
import { defineComponent } from "@vue/composition-api";

export default defineComponent({
  name: "Schedule",
  props: {
    schedules: {
      type: Array,
      require: false,
    },
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
* {
  font-family: Spoqa Han Sans Neo;
}

.scheduleArea {
  .scheduleTitle {
    font-weight: 700;
  }

  .schedule {
    box-sizing: border-box;
  }
}

@include desktop {
  .scheduleArea {
    .scheduleTitle {
      font-size: 32px;
      line-height: 48px;
    }

    .schedules {
      display: block;
      overflow-x: auto;
      white-space: nowrap;
      margin-top: 16px;

      .schedule {
        min-width: 200px;
        display: inline-block;
        margin-right: 16px;
      }
    }
  }
}

@include tablet {
  .scheduleArea {
    .scheduleTitle {
      margin-left: 64px;
      font-size: 32px;
      line-height: 48px;
    }

    .schedules {
      display: block;
      overflow-x: auto;
      white-space: nowrap;
      margin-top: 16px;
      &::-webkit-scrollbar {
        display: none;
      }

      .schedule {
        width: 200px;
        display: inline-block;
        margin-right: 16px;

        &:last-child {
          margin-right: 64px;
        }

        &:first-child {
          margin-left: 64px;
        }
      }
    }
  }
}

@include mobile {
  .scheduleArea {
    .scheduleTitle {
      font-size: 24px;
      line-height: 36px;
    }

    .schedules {
      display: flex;
      flex-direction: column;
      margin-top: 8px;

      .schedule {
        width: 100%;
        margin-top: 8px;
      }
    }
  }
}
</style>
