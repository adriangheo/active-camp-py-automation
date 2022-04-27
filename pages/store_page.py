from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator

class StorePage(BasePage):
    url = 'https://tstprep.com/store/'

    @property
    def courses_for_duolingo(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Courses for the Duolingo English Test')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def private_lessons_for_duolingo(self):
        lctr = Locator(By.CSS_SELECTOR, "html body.bp-nouveau.page-template-default.page.page-id-124677.page-parent.theme-buddyboss-theme.et_divi_builder.woocommerce-shop.woocommerce-js.buddyboss-theme.bb-custom-typo.et-pb-theme-buddyboss.child.et-db.js.bb-page-loaded.gecko div#page.site div#content.site-content div.container div.bb-grid.site-content-grid div#primary.content-area.bb-grid-cell main#main.site-main article#post-124677.post-124677.page.type-page.status-publish.hentry div.entry-content div#et-boc.et-boc div#et_builder_outer_content.et_builder_outer_content div.et-l.et-l--post div.et_builder_inner_content.et_pb_gutters3 div.et_pb_with_border.et_pb_section.et_pb_section_1.content-section-wh.et_section_regular.et_section_transparent div.et_pb_row.et_pb_row_2.store-row4.det-store-row.et_pb_gutters2.et_pb_row_4col div.et_pb_column.et_pb_column_1_4.et_pb_column_3.et_clickable.et_pb_css_mix_blend_mode_passthrough div.et_pb_module.et_pb_image.et_pb_image_1.storebox-img")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def score_evaluation_for_duolingo(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Score Evaluation for the Duolingo English Test')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def complete_practice_test_pack(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Complete Practice')]][text()[contains(.,'Test Pack')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def emergency_course(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Emergency')]][text()[contains(.,'Course')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def score_builder_program(self):
        lctr = Locator(By.XPATH,"//h3[text()[contains(.,'Score Builder')]][text()[contains(.,'Program')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def private_lessons_1_4_sections(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Private Lessons')]][text()[contains(.,'1-4 sections')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def trial_lesson(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Trial')]][text()[contains(.,'Lesson')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def speaking_evaluation(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Speaking')]][text()[contains(.,'Evaluation')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def writing_essay_evaluations(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Writing')]][text()[contains(.,'Essay Evaluations')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def reading_group_classes(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Reading')]][text()[contains(.,'Group Classes')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def listening_group_classes(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Listening')]][text()[contains(.,'Group Classes')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def speaking_group_classes(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Speaking')]][text()[contains(.,'Group Classes')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def writing_group_classes(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Writing')]][text()[contains(.,'Group Classes')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def reading_practice_pack(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Reading')]][text()[contains(.,'Practice Pack')]]")
        return BaseElement(driver = self.driver, locator=lctr)
    @property
    def listening_practice_pack(self):
        lctr = Locator(By.XPATH, "//h3[text()[contains(.,'Listening')]][text()[contains(.,'Practice Pack')]]")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def first_pricebox_btn(self):
        lctr = Locator(By.CSS_SELECTOR, ".pricebox-button:nth-child(0)")
        return BaseElement(driver = self.driver, locator=lctr)

    @property
    def second_pricebox_btn(self):
        lctr = Locator(By.CSS_SELECTOR, ".pricebox-button:nth-child(1)")
        return BaseElement(driver = self.driver, locator=lctr)