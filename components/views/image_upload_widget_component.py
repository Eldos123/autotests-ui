from playwright.sync_api import Page, expect

from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.button import Button
from elements.file_input import FileInput
from elements.icon import Icon
from elements.image import Image
from elements.input import Input
from elements.text import Text


class ImageUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        self.preview_image = Image(page, f'{identifier}-image-upload-widget-preview-image', 'Preview Image')

        self.image_upload_info_icon = Icon(page,f'{identifier}-image-upload-widget-info-icon', 'Icon')
        self.image_upload_info_title = Text(page, f'{identifier}-image-upload-widget-info-title-text', 'Title')
        self.image_upload_info_description = Text(
            page,
            f'{identifier}-image-upload-widget-info-description-text',
            'Description'
        )

        self.upload_button = Button(page,f'{identifier}-image-upload-widget-upload-button', 'Upload button')
        self.remove_button = Button(page, f'{identifier}-image-upload-widget-remove-button', 'Remove button')
        self.upload_input = FileInput(page, f'{identifier}-image-upload-widget-input', 'Upload Input')

    # Проверяет отображение виджета в зависимости от наличия загруженного изображения
    def check_visible(self, is_image_uploaded: bool = False):
        expect(self.image_upload_info_icon.get_locator()).to_be_visible()

        expect(self.image_upload_info_title.get_locator()).to_be_visible()
        expect(self.image_upload_info_title.get_locator()).to_have_text(
            'Tap on "Upload image" button to select file'
        )

        expect(self.image_upload_info_description.get_locator()).to_be_visible()
        expect(self.image_upload_info_description.get_locator()).to_have_text('Recommended file size 540X300')

        expect(self.upload_button.get_locator()).to_be_visible()

        if is_image_uploaded:
            # Если картинка загружена, проверяем состояние специфичное для загруженной картинки
            expect(self.remove_button.get_locator()).to_be_visible()
            expect(self.preview_image.get_locator()).to_be_visible()

        if not is_image_uploaded:
            # Если картинка yt загружена, проверяем наличие компонента EmptyViewComponent
            self.preview_empty_view.check_visible(
                title='No image selected',
                description='Preview of selected image will be displayed here'
            )

    def click_remove_image_button(self):
        self.remove_button.click()

    def upload_preview_image(self, file: str):
        self.upload_input.set_input_files(file)