<template>
  <div
    :id="project.idx"
    class="project-card-component-container"
    @click="showDetail(project)"
  >
    <nuxt-link
      :to="{ path: '/project', hash: `#${project.idx}` }"
      @click.native="scrollToId(project.idx)"
    >
      <img class="thumbnail" :data-src="thumbnail" v-lazy-load />
      <p class="name">{{ project.app_name }}</p>
      <p class="time">{{ project.th }}th | {{ project.year }}</p>
    </nuxt-link>
    <div class="links">
      <div
        v-for="(link, platform) in project.link"
        :key="platform"
        class="link-item"
        @click="onClickLink(link)"
        @click.stop=""
      >
        <a :href="link">
          {{ platform }}
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent } from "@nuxtjs/composition-api";
import { mapActions } from "vuex";
const ProjectCard = defineComponent({
  name: "ProjectCard",
  props: {
    project: {
      type: Object,
      required: true,
    },
  },
  computed: {
    thumbnail() {
      return this.project.thumbnail || "/no-image.svg";
    },
  },
  methods: {
    ...mapActions({ showDetail: "project/showDetail" }),
    onClickLink(href) {
      window.location.href = href;
    },
    scrollToId(id) {
      document.getElementById(id).scrollIntoView();
    },
  },
});

export default ProjectCard;
</script>

<style lang="scss" scoped>
@import "~/assets/css/_device.scss";
@import "~/assets/css/setting.scss";

* {
  font-family: Spoqa Han Sans Neo;
}
.project-card-component-container {
  display: flex;
  flex-direction: column;
  border: solid 1px $border-default;

  .links {
    margin: auto 0 0;
  }
}

.name {
  cursor: pointer;
}
a {
  text-decoration: none;
}

.thumbnail {
  object-fit: cover;
}

.link-item {
  &:hover {
    transition: 0.3s;
    background: $background-sub;
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

@include d-c3 {
  .thumbnail {
    width: 100%;
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
  }

  .name {
    margin: 24px 0 0 24px;
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: 36px;
    letter-spacing: -0.02em;
    color: $text-default;
  }
  .time {
    margin: 8px 0 0 24px;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 27px;
    color: $text-sub;
  }

  .links {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 24px;
    .link-item {
      margin-right: 8px;
      a {
        font-weight: bold;
        font-size: 18px;
        line-height: 27px;
        text-align: center;
        letter-spacing: -0.02em;
        color: $text-default;
      }
      padding: 16px 24px;
      width: 100%;
      text-align: center;
      border-radius: 8px;
      border: 1px solid $border-default;
      cursor: pointer;
    }
    .link-item:last-child {
      margin: 0;
    }
  }
}

@include d-c2 {
  .project {
    flex-basis: 364.5px;
    .thumbnail {
      width: 100%;
      border-top-left-radius: 16px;
      border-top-right-radius: 16px;
    }

    .name {
      margin: 24px 0 0 24px;
      font-style: normal;
      font-weight: bold;
      font-size: 24px;
      line-height: 36px;
      letter-spacing: -0.02em;
      color: $text-default;
    }
    .time {
      margin: 8px 0 0 24px;
      font-style: normal;
      font-weight: normal;
      font-size: 18px;
      line-height: 27px;
      color: $text-sub;
    }
    .links {
      display: flex;
      flex-direction: row;
      justify-content: space-between;
      padding: 24px;
      .link-item {
        margin-right: 8px;
        a {
          font-weight: bold;
          font-size: 18px;
          line-height: 27px;
          text-align: center;
          letter-spacing: -0.02em;
          color: $text-default;
        }
        padding: 16px 24px;
        width: 100%;
        text-align: center;
        border-radius: 8px;
        border: 1px solid $border-default;
        cursor: pointer;
      }
      .link-item:last-child {
        margin: 0;
      }
    }
  }
}

@include d-c1 {
  .thumbnail {
    width: 100%;
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
  }
  .name {
    margin: 24px 0 0 24px;
    font-style: normal;
    font-weight: bold;
    font-size: 24px;
    line-height: 36px;
    letter-spacing: -0.02em;
    color: $text-default;
  }
  .time {
    margin: 8px 0 0 24px;
    font-style: normal;
    font-weight: normal;
    font-size: 18px;
    line-height: 27px;
    color: $text-sub;
  }
  .links {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 24px;
    .link-item {
      margin-right: 8px;
      a {
        font-weight: bold;
        font-size: 18px;
        line-height: 27px;
        text-align: center;
        letter-spacing: -0.02em;
        color: $text-default;
      }
      padding: 16px 24px;
      width: 100%;
      text-align: center;
      border-radius: 8px;
      border: 1px solid $border-default;
      cursor: pointer;
    }
    .link-item:last-child {
      margin: 0;
    }
  }
}

@include m-c2 {
  .thumbnail {
    width: 100%;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
  }
  .name {
    margin: 16px 0 0 16px;
    font-style: normal;
    font-weight: bold;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: -0.02em;
    color: $text-default;
  }
  .time {
    margin: 8px 0 0 16px;
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 21px;
    color: $text-sub;
  }
  .links {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 16px;
    .link-item {
      margin-right: 8px;
      a {
        font-weight: bold;
        font-size: 14px;
        line-height: 21px;
        text-align: center;
        letter-spacing: -0.02em;
        color: $text-default;
      }
      padding: 12px 0 12px 0;
      width: 100%;
      text-align: center;
      border-radius: 4px;
      border: 1px solid $border-default;
      cursor: pointer;
    }
    .link-item:last-child {
      margin: 0;
    }
  }
}

@include m-c1 {
  .thumbnail {
    width: 100%;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
  }
  .name {
    margin: 16px 0 0 16px;
    font-style: normal;
    font-weight: bold;
    font-size: 16px;
    line-height: 24px;
    letter-spacing: -0.02em;
    color: $text-default;
  }
  .time {
    margin: 8px 0 0 16px;
    font-style: normal;
    font-weight: normal;
    font-size: 14px;
    line-height: 21px;
    color: $text-sub;
  }
  .links {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 16px;
    .link-item {
      margin-right: 8px;
      a {
        font-weight: bold;
        font-size: 14px;
        line-height: 21px;
        text-align: center;
        letter-spacing: -0.02em;
        color: $text-default;
      }
      padding: 12px 0 12px 0;
      width: 100%;
      text-align: center;
      border-radius: 4px;
      border: 1px solid $border-default;
      cursor: pointer;
    }
    .link-item:last-child {
      margin: 0;
    }
  }
}
</style>
