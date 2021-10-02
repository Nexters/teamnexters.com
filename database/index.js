import { Database } from "@vuex-orm/core";
import Project from "@/models/project";

const database = new Database();

database.register(Project);

export default database;
