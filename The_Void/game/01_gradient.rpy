init python:
    renpy.register_shader("gradient_overlay", variables="""
        uniform vec4 u_gradient_top;
        uniform vec4 u_gradient_bottom;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
    """, fragment_300="""
        float pos = v_tex_coord.y;
        vec4 grad = mix(u_gradient_top, u_gradient_bottom, pos);
        vec3 res;
        
        
        if (gl_FragColor.r < 0.5) res.r = 2.0 * gl_FragColor.r * grad.r;
        else res.r = 1.0 - 2.0 * (1.0 - gl_FragColor.r) * (1.0 - grad.r);
        
        if (gl_FragColor.g < 0.5) res.g = 2.0 * gl_FragColor.g * grad.g;
        else res.g = 1.0 - 2.0 * (1.0 - gl_FragColor.g) * (1.0 - grad.g);
        
        if (gl_FragColor.b < 0.5) res.b = 2.0 * gl_FragColor.b * grad.b;
        else res.b = 1.0 - 2.0 * (1.0 - gl_FragColor.b) * (1.0 - grad.b);
        
        gl_FragColor.rgb = mix(gl_FragColor.rgb, res, grad.a);
        gl_FragColor.rgb = gl_FragColor.rgb * gl_FragColor.a;
    """)

    def hex_to_gl(hex_str):
        h = hex_str.lstrip('#')
        if len(h) == 8:
            return tuple(int(h[i:i+2], 16)/255.0 for i in (0, 2, 4, 6))
        return tuple(int(h[i:i+2], 16)/255.0 for i in (0, 2, 4)) + (1.0,)

# --- SILNIK GRADIENTU ---
transform apply_grad(t="#ffffff", b="#000000"):
    shader "gradient_overlay"
    u_gradient_top hex_to_gl(t)
    u_gradient_bottom hex_to_gl(b)

#tint
transform night_tint:
    matrixcolor TintMatrix("#132f4b8e")
transform day_tint:
    matrixcolor TintMatrix("#ffe08b50")
transform sunset_tint:
    matrixcolor TintMatrix("#a3642a")
transform crystal_tint:
    matrixcolor TintMatrix("#9668d35d")
transform water_tint:
    matrixcolor TintMatrix("#35806442")

#gradient
transform grad_night:
    apply_grad(t="#83e6ff67", b="#0d0e41")
transform grad_sunset:
    apply_grad(t="#ffaa5588", b="#331100")
transform grad_day:
    apply_grad(t="#44444466", b="#000000")
transform grad_crystal:
    apply_grad(t="#ff00f24f", b="#00b7ff63")
transform grad_water:
    apply_grad(t="#ff00f24f", b="#00b7ff63")


#połaczone
transform night:
    grad_night
    night_tint

transform sunset:
    grad_sunset
    sunset_tint

transform day:
    grad_day
    day_tint

transform crystal:
    grad_crystal
    crystal_tint


transform water:
    grad_water
    water_tint