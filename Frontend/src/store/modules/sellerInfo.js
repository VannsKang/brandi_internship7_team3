// SECTION initial state
const state = () => ({
  sellerInfo_header: {
    title: "셀러 정보 수정페이지",
    sub_title: "셀러 정보 조회 / 수정",
    breadcrumb: ["회원 관리", "셀러 계정 관리", "셀러 정보 조회 / 수정"],
  },

  product_enroll_header: {
    title: "갓포스트맨",
    sub_title: "원래 프로덕트 등록이어야 했던거 / 브랜디 위코드 3팀",
    breadcrumb: ["성규원", "김동현", "강수명"],
  },
});

// SECTION getters
const getters = {
  //
};

// SECTION mutations
const mutations = {
  //
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
};
