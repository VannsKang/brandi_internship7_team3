import Login from "../components/Login/Login.vue";
import Signup from "../components/Signup/Signup.vue";
import Main from "../components/Main/Main.vue";

export default [
  { path: "/", name: "Login", component: Login },
  { path: "/signup", name: "Signup", component: Signup },
  { path: "/main", name: "Main", component: Main },
];
