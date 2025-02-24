import pygame
import pygame_gui

class UserInterface:
    def __init__(self, screen_res):
        self.manager = pygame_gui.UIManager(screen_res)
        self.pause_menu = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                screen_res[0]//2 - 150,
                screen_res[1]//2 - 100,
                300, 200
            ),
            manager=self.manager
        )
        self.resume_btn = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(50, 50, 200, 40),
            text="Resume",
            container=self.pause_menu,
            manager=self.manager
        )

    def handle_events(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.resume_btn:
                    return "resume"
        self.manager.process_events(event)

    def draw(self, surface):
        self.manager.draw_ui(surface)
