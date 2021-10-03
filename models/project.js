import { Model } from "@vuex-orm/core";
export default class Project extends Model {
  static entity = "projects";
  static primaryKey = "idx";
  static fields() {
    return {
      idx: this.attr(null),
      app_name: this.string(),
      thumbnail: this.string(),
      th: this.string(),
      year: this.string(),
      team_name: this.string(),
      members: this.string(),
      description: this.string(),
      ppt: this.string(),
      link: this.string(),
    };
  }
}
