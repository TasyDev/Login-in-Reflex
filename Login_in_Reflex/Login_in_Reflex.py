import reflex as rx

# Estilos globales
style_navbar = {
    "rx.link": {
        "text_decoration": "none",
        "color": "#333",
        "font_weight": "500",
        "_hover": {"color": "blue"},
    }
}

class State(rx.State):
    """Estado para manejar la visibilidad y animación interna."""
    is_login: bool = True

    def toggle_auth(self):
        """Cambia entre Login y Registro."""
        self.is_login = not self.is_login

def navbar() -> rx.Component:
    return rx.flex(
        rx.hstack(
            rx.link("Home", href="/"),
            rx.link("About", href="/about"),
            rx.link("Services", href="/services"),
            rx.link("Contact", href="/contact"),
            spacing="5",
        ),
        justify_content="space-between",
        align_items="center",
        padding="1rem 2rem",
        background_color="rgba(245, 245, 245, 0.8)",
        backdrop_filter="blur(10px)",
        width="100%",
        position="fixed",
        top="0",
        z_index="10",
    )

def auth_form() -> rx.Component:
    return rx.vstack(
        # Título dinámico
        rx.heading(
            rx.cond(State.is_login, "Iniciar Sesión", "Crear Cuenta"),
            size="8",
            margin_bottom="1rem"
        ),
        
        # Campos comunes
        rx.input(placeholder="Correo Electrónico", width="100%", size="3"),
        rx.input(placeholder="Contraseña", type="password", width="100%", size="3"),
        
        # Campo extra solo para Registro
        rx.cond(
            ~State.is_login,
            rx.input(placeholder="Confirmar Contraseña", type="password", width="100%", size="3"),
        ),
        
        # Botón principal
        rx.button(
            rx.cond(State.is_login, "Entrar", "Registrarse"),
            color_scheme="blue",
            width="100%",
            size="3",
            margin_top="1rem"
        ),
        
        # Switch interno (La animación ocurre aquí al cambiar el contenido)
        rx.hstack(
            rx.text(rx.cond(State.is_login, "¿No tienes cuenta?", "¿Ya tienes cuenta?")),
            rx.button(
                rx.cond(State.is_login, "Regístrate", "Loguéate"),
                variant="ghost",
                on_click=State.toggle_auth,
            ),
            font_size="0.9rem",
            margin_top="1rem"
        ),
        
        padding="3rem",
        background="white",
        border_radius="20px",
        box_shadow="0 10px 25px rgba(0,0,0,0.1)",
        width="400px",
        transition="all 0.3s ease", # Animación interna de tamaño y contenido
    )

def container() -> rx.Component:
    return rx.center(
        rx.hstack(
            # Texto descriptivo persistente
            rx.vstack(
                rx.heading("Bienvenido", size="9", color="white"),
                rx.text(
                    "Gestiona tu cuenta de forma segura y rápida.",
                    size="4",
                    color="white",
                    opacity="0.9"
                ),
                align_items="start",
                max_width="400px",
                spacing="4",
            ),
            
            # El formulario único con lógica interna
            auth_form(),
            
            spacing="9",
            width="100%",
            max_width="1000px",
            padding="2rem",
        ),
        width="100%",
        height="100vh",
    )

def fondo() -> rx.Component:
    return rx.box(
        style={
            "position": "fixed",
            "top": "0",
            "left": "0",
            "width": "100%",
            "height": "100vh",
            "background": "url(https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&q=80&w=2070) no-repeat",
            "background_size": "cover",
            "background_position": "center",
            "filter": "blur(8px)",
            "z_index": "-1",
        },
    )

@rx.page(route="/", title="Login")
def login() -> rx.Component:
    return rx.box(
        fondo(),
        navbar(),   
        container(),
        width="100%",
    )

app = rx.App(style=style_navbar)
