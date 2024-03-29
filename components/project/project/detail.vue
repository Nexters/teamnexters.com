<template>
  <div class="modal" :class="{ invisible: !showDetail }">
    <div class="project-detail-container" role="dialog">
      <div class="toolbar">
        <img
          class="leading"
          src="~/assets/img/ic_back.svg"
          @click="dismiss()"
        />
        <img
          class="trailing"
          src="~/assets/img/ic_close.svg"
          @click="dismiss()"
        />
      </div>
      <div class="contents">
        <div class="information">
          <h1 class="name">{{ project.app_name }}</h1>
          <div class="th-year">{{ project.th }}{{ th_text }} | {{ project.year }}</div>
          <div class="team-members">
            TEAM {{ project.team_name }} | {{ members }}
          </div>
        </div>
        <div class="thumbnail"><img :data-src="thumbnail" v-lazy-load /></div>
        <div class="description">{{ project.description }}</div>
        <ArrowButton
          v-show="project.ppt"
          :href="project.ppt || ''"
          text="최종 발표 자료"
          :size="ppt_link_size"
          :isWhite="false"
        />
      </div>
      <div class="links">
        <a
          v-for="(link, platform) in project.link"
          :key="platform"
          class="link-item"
          :href="link"
          target="_blank"
        >
          {{ platform }}
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
import { mapGetters, mapActions } from "vuex";
export default defineComponent({
  name: "ProjectDetail",
  props: {
    project: {
      type: Object,
      required: true,
    },
  },
  computed: {
    ...mapGetters({
      showDetail: "project/showDetail",
    }),
    ppt_link_size() {
      return this.$mq === "mobile" ? 16 : 24;
    },
    members() {
      return this.project.members?.join(" ") || "";
    },
    thumbnail() {
      return this.project.thumbnail || "/no-image.svg";
    },
    th_text() {
      const last_digit = this.project.th % 10;
      if (last_digit === 1) {
        return 'st';
      } else if (last_digit === 2) {
        return 'nd';
      } else if (last_digit === 3) {
        return 'rd';
      } else {
        return 'th';
      }
    },
  },
  methods: {
    ...mapActions({
      dismiss: "project/dismiss",
    }),
  },
});
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";

* {
  font-family: Spoqa Han Sans Neo;
}
.invisible {
  display: none;
}

.contents {
  .thumbnail {
    > img {
      border: 1px solid $border-default;
    }
  }
}
.link-item {
  &:hover {
    transition: 0.3s;
    background: $background-hover;
  }
  &:active {
    transition: 0.3s;
    background: $background-active;
  }
  &:disabled {
    cursor: not-allowed;
    pointer-events: none;
    background: $background-sub;
    color: $text-disable;
  }
}

.toolbar {
  height: 56px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  background-color: white;
  border-radius: 16px;
  .leading {
    margin: 16px;
    height: 24px;
    width: 24px;
    cursor: pointer;
  }
  .trailing {
    margin: 16px;
    height: 24px;
    width: 24px;
    cursor: pointer;
  }
  @include mobile {
    .leading {
      display: block;
    }
    .trailing {
      display: none;
    }
  }
  @include tablet {
    .leading {
      display: none;
    }
    .trailing {
      margin-left: auto;
      display: block;
    }
  }
  @include desktop {
    .leading {
      display: none;
    }
    .trailing {
      margin-left: auto;
      display: block;
    }
  }
}
@include desktop {
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000;
    overflow-y: auto;
  }

  .project-detail-container {
    border-radius: 16px;
    position: relative;
    width: 528px;
    display: flex;
    flex-direction: column;
    background-color: $background-default;
    margin: 30px auto;

    .contents {
      padding: 24px;
      display: flex;
      flex-direction: column;
      > div {
        margin-bottom: 16px;
      }
      > div:last-child {
        margin: 0;
      }
    }
    .information {
      display: flex;
      flex-direction: column;
      > div {
        margin-top: 8px;
      }
    }
    .name {
      font-style: normal;
      font-weight: bold;
      font-size: 32px;
      line-height: 48px;
      letter-spacing: -0.02em;

      color: $text-default;
    }
    .th-year {
      font-style: normal;
      font-weight: normal;
      font-size: 14px;
      line-height: 21px;
      letter-spacing: -0.02em;

      color: $text-sub;
    }
    .team-members {
      font-style: normal;
      font-weight: normal;
      font-size: 18px;
      line-height: 27px;
      letter-spacing: -0.02em;

      color: $text-default;
    }
    .thumbnail {
      img {
        width: 480px;
        height: 270px;
        border-radius: 16px;
      }
    }
    .description {
      white-space: pre-wrap;

      font-style: normal;
      font-weight: normal;
      font-size: 18px;
      line-height: 27px;
      letter-spacing: -0.02em;

      color: $text-default;
    }
    .ppt {
      display: flex;
      width: 172px;
      cursor: pointer;
      padding: 16px 0;

      p {
        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 36px;
        letter-spacing: -0.02em;

        color: $text-default;
      }
      img {
        width: 24px;
        height: 24px;
        margin-left: 8px;
        align-self: center;
      }
    }
    a {
      text-decoration: none;
    }
    .links {
      margin: 0 24px 24px;
      display: flex;
      flex-direction: row;
      justify-content: space-between;
    }
    .link-item {
      font-weight: bold;
      font-size: 16px;
      line-height: 24px;
      text-align: center;
      letter-spacing: -0.02em;

      color: $text-default;
      width: 100%;
      height: 45px;
      line-height: 45px;
      text-align: center;
      border: 1px solid $border-default;
      border-radius: 8px;
      margin-right: 8px;
      cursor: pointer;
    }
    .link-item:last-child {
      margin: 0;
    }
  }
}
@include mobile {
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 1000;
  }
  .project-detail-container {
    height: 100%;
    display: flex;
    flex-direction: column;
    background-color: $background-default;
    overflow-y: auto;

    @include desktop {
      .thumbnail {
        width: 100%;
        height: 445px;
      }
    }
    .contents {
      padding: 24px;
      display: flex;
      flex-direction: column;
      > div {
        margin-bottom: 16px;
      }
      > div:last-child {
        margin: 0;
      }
    }
    .information {
      display: flex;
      flex-direction: column;
      > div {
        margin-top: 4px;
      }
    }
    .name {
      font-style: normal;
      font-weight: bold;
      font-size: 24px;
      line-height: 36px;
      letter-spacing: -0.02em;

      color: $text-default;
    }
    .th-year {
      font-style: normal;
      font-weight: normal;
      font-size: 12px;
      line-height: 18px;
      letter-spacing: -0.02em;

      color: $text-sub;
    }
    .team-members {
      font-style: normal;
      font-weight: normal;
      font-size: 14px;
      line-height: 21px;
      letter-spacing: -0.02em;

      color: $text-default;
    }
    .thumbnail {
      width: 100%;

      img {
        width: 100%;
        max-height: 445px;
        border-radius: 8px;
      }
    }
    .description {
      white-space: pre-wrap;

      font-style: normal;
      font-weight: normal;
      font-size: 14px;
      line-height: 21px;
      letter-spacing: -0.02em;

      color: $text-default;
    }
    .ppt {
      display: flex;
      width: 130px;
      cursor: pointer;
      padding: 8px 0;

      p {
        font-style: normal;
        font-weight: bold;
        font-size: 16px;
        line-height: 24px;
        letter-spacing: -0.02em;

        color: $text-default;
      }
      img {
        width: 16px;
        height: 16px;
        align-self: center;
        margin-left: 8px;
      }
    }
    a {
      text-decoration: none;
    }
    .links {
      margin: 0 24px 24px 24px;

      display: flex;
      flex-direction: row;
      justify-content: space-between;
    }
    .link-item {
      font-weight: bold;
      font-size: 16px;
      line-height: 24px;
      text-align: center;
      letter-spacing: -0.02em;

      color: $text-default;
      width: 100%;
      height: 45px;
      line-height: 45px;
      text-align: center;
      border: 1px solid $border-default;
      border-radius: 4px;
      margin-right: 8px;
      cursor: pointer;
    }
    .link-item:last-child {
      margin: 0;
    }
  }
}
@include tablet {
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000;
    overflow-y: auto;
  }

  .project-detail-container {
    border-radius: 16px;
    position: relative;
    width: 528px;
    display: flex;
    flex-direction: column;
    background-color: $background-default;
    margin: 30px auto;

    .contents {
      padding: 24px;
      display: flex;
      flex-direction: column;
      > div {
        margin-bottom: 16px;
      }
      > div:last-child {
        margin: 0;
      }
    }
    .information {
      display: flex;
      flex-direction: column;
      > div {
        margin-top: 8px;
      }
    }
    .name {
      font-style: normal;
      font-weight: bold;
      font-size: 32px;
      line-height: 48px;
      letter-spacing: -0.02em;

      color: $text-default;
    }
    .th-year {
      font-style: normal;
      font-weight: normal;
      font-size: 14px;
      line-height: 21px;
      letter-spacing: -0.02em;

      color: $text-sub;
    }
    .team-members {
      font-style: normal;
      font-weight: normal;
      font-size: 18px;
      line-height: 27px;
      letter-spacing: -0.02em;

      color: $text-default;
    }
    .thumbnail {
      img {
        width: 480px;
        height: 270px;
        border-radius: 16px;
      }
    }
    .description {
      white-space: pre-wrap;

      font-style: normal;
      font-weight: normal;
      font-size: 18px;
      line-height: 27px;
      letter-spacing: -0.02em;

      color: $text-default;
    }
    .ppt {
      display: flex;
      width: 172px;
      cursor: pointer;
      padding: 16px 0;

      p {
        font-style: normal;
        font-weight: bold;
        font-size: 24px;
        line-height: 36px;
        letter-spacing: -0.02em;

        color: $text-default;
      }
      img {
        width: 24px;
        height: 24px;
        margin-left: 8px;
        align-self: center;
      }
    }
    a {
      text-decoration: none;
    }
    .links {
      margin: 0 24px 24px;
      display: flex;
      flex-direction: row;
      justify-content: space-between;
    }
    .link-item {
      font-weight: bold;
      font-size: 16px;
      line-height: 24px;
      text-align: center;
      letter-spacing: -0.02em;

      color: $text-default;
      width: 100%;
      height: 45px;
      line-height: 45px;
      text-align: center;
      border: 1px solid $border-default;
      border-radius: 8px;
      margin-right: 8px;
      cursor: pointer;
    }
    .link-item:last-child {
      margin: 0;
    }
  }
}
</style>
