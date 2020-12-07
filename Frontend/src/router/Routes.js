import Login from "../components/Login/Login.vue";
import Signup from "../components/Signup/Signup.vue";
import Main from "../components/Main/Main.vue";
import Sellers from "../components/Sellers/Sellers.vue";
import SellerInfo from "../components/SellerInfo/SellerInfo.vue";
import Products from "../components/Products/Products.vue";
import Page403 from "../components/components/Page-403/Page-403.vue";

export default [
  { path: "/", name: "Login", component: Login },
  { path: "/signup", name: "Signup", component: Signup },
  { path: "/403", name: "Page403", component: Page403 },
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
      {
        path: "seller/info/:id",
        name: "Info",
        component: SellerInfo,
      },
      {
        path: "products",
        name: "Products",
        component: Products,
      },
    ],
  },
];
