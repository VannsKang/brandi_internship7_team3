// SECTION initial state
const state = () => ({
  menuItems: [
    {
      menu_id: "sub1",
      menu_name: "통계",
      menu_icon: "bar-chart",
      sub_menus: [{ id: 2, name: "시간단위분석", link: "chart" }],
    },
    {
      menu_id: "sub2",
      menu_name: "주문관리",
      menu_icon: "shopping-cart",
      sub_menus: [
        { id: 3, name: "결제완료관리", link: "payment" },
        { id: 4, name: "상품준비관리", link: "product" },
        { id: 5, name: "배송중관리", link: "shipping" },
        { id: 6, name: "배송완료관리", link: "shipping_complete" },
        { id: 7, name: "구매확정관리", link: "order_complete" },
      ],
    },
    {
      menu_id: "sub3",
      menu_name: "취소/환불 관리",
      menu_icon: "frown",
      sub_menus: [
        { id: 8, name: "환불요청관리", link: "refund_request" },
        { id: 9, name: "환불완료관리", link: "refund_complete" },
        { id: 10, name: "주문취소완료관리", link: "cancel_complete" },
      ],
    },
    {
      menu_id: "sub4",
      menu_name: "상품관리",
      menu_icon: "shopping",
      sub_menus: [
        { id: 11, name: "상품 관리", link: "product_manage" },
        { id: 12, name: "상품 등록", link: "product_enroll" },
      ],
    },
    {
      menu_id: "sub5",
      menu_name: "고객응대관리",
      menu_icon: "smile",
      sub_menus: [
        { id: 13, name: "Q&A 관리", link: "question" },
        { id: 14, name: "텍스트 리뷰", link: "review" },
      ],
    },
    {
      menu_id: "sub6",
      menu_name: "기획전/쿠폰관리",
      menu_icon: "gift",
      sub_menus: [
        { id: 15, name: "기획전 관리", link: "event" },
        { id: 16, name: "쿠폰 관리", link: "coupon" },
      ],
    },
    {
      menu_id: "sub7",
      menu_name: "회원관리",
      menu_icon: "user",
      sub_menus: [
        { id: 17, name: "회원관리_커뮤니티", link: "user" },
        { id: 18, name: "셀러 계정 관리", link: "seller" },
      ],
    },
  ],
});

// getters
const getters = {
  //
};

// mutations
const mutations = {
  //
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
};
