init python:
    renpy.register_shader("gradient_overlay", variables="""
        uniform vec4 u_gradient_top;
        uniform vec4 u_gradient_bottom;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
    """, vertex_300="""
        v_tex_coord = a_tex_coord;
    """, fragment_300="""
        vec4 orig = gl_FragColor;
        
        
        if (orig.a < 0.0001) {
            discard;
        }

       
        vec3 base = clamp(orig.rgb / orig.a, 0.0, 1.0);

        float pos = v_tex_coord.y;
        vec4 grad = mix(u_gradient_top, u_gradient_bottom, pos);
        
        vec3 res;

        if (grad.r < 0.5) res.r = base.r + (2.0 * grad.r - 1.0) * (base.r - base.r * base.r);
        else res.r = base.r + (2.0 * grad.r - 1.0) * (sqrt(base.r) - base.r);
        
        if (grad.g < 0.5) res.g = base.g + (2.0 * grad.g - 1.0) * (base.g - base.g * base.g);
        else res.g = base.g + (2.0 * grad.g - 1.0) * (sqrt(base.g) - base.g);
        
        if (grad.b < 0.5) res.b = base.b + (2.0 * grad.b - 1.0) * (base.b - base.b * base.b);
        else res.b = base.b + (2.0 * grad.b - 1.0) * (sqrt(base.b) - base.b);
        
      
        vec3 final_rgb = mix(base, res, grad.a);
        
        
        gl_FragColor.rgb = final_rgb * orig.a;
    """)
    def hex_to_gl(hex_str):
        h = hex_str.lstrip('#')
        if len(h) == 8:
            return tuple(int(h[i:i+2], 16)/255.0 for i in (0, 2, 4, 6))
        return tuple(int(h[i:i+2], 16)/255.0 for i in (0, 2, 4)) + (1.0,)

# --- SILNIK GRADIENTU ---
transform apply_grad(t="#80808000", b="#80808000"):
    shader "gradient_overlay"
    u_gradient_top hex_to_gl(t)
    u_gradient_bottom hex_to_gl(b)

#tint
transform night_tint:
    matrixcolor TintMatrix("#2c4c6b69")
transform day_tint:
    matrixcolor TintMatrix("#ffffff00")
transform sunset_tint:
    matrixcolor TintMatrix("#0073ff")
transform crystal_tint:
    matrixcolor TintMatrix("#9668d35d")
transform water_tint:
    matrixcolor TintMatrix("#0b412f7c")

#gradient
transform grad_night:
    apply_grad(t="#def8ff93", b="#121331ff")
transform grad_sunset:
    apply_grad(t="#ff0000ff", b="#22ff00ff")
transform grad_day:
    apply_grad(t="#f0ddb398", b="#66422469")
transform grad_crystal:
    apply_grad(t="#ff2cf483", b="#00b7ff88")
transform grad_water:
    apply_grad(t="#7ebaffa4", b="#0b221598")


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