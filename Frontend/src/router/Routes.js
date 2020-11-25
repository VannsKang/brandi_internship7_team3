import Login from "../components/Login/Login.vue";
import Signup from "../components/Signup/Signup.vue";
import Main from "../components/Main/Main.vue";
import Sellers from "../components/Sellers/Sellers.vue";

export default [
  { path: "/", name: "Login", component: Login },
  { path: "/signup", name: "Signup", component: Signup },
  {
    path: "/:name",
    name: "Main",
    component: Main,
    children: [
      {
        path: "seller",
        name: "Sellers",
        component: Sellers,
      },
    ],
  },
];
