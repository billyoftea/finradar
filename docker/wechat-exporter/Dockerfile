FROM ghcr.io/wechat-article/wechat-article-exporter:latest

USER root

# 为了支持 http://<公网IP>/ 登录场景，移除登录链路 cookie 的 Secure 标记。
# 背景：浏览器在 HTTP 下不会发送 Secure cookie，会导致 /api/web/login/getqrcode 返回空内容。
RUN set -eux; \
    file=/app/server/chunks/nitro/nitro.mjs; \
    sed -i 's|x=l.headers.getSetCookie().filter(t=>t.startsWith("uuid="));|x=l.headers.getSetCookie().filter(t=>t.startsWith("uuid=")).map(t=>t.replace(/;\\s*Secure/ig,""));|g' "$file"; \
    sed -i 's|; Secure; HttpOnly|; HttpOnly|g' "$file"; \
    grep -q 'filter(t=>t.startsWith("uuid=")).map(t=>t.replace(/;' "$file"

USER node

ENTRYPOINT ["node", "server/index.mjs"]
