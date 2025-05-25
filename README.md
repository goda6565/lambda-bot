# ArXiv論文要約Bot

このプロジェクトは、Slack上で動作するArXiv論文要約Botの実装です。ユーザーがArXivの論文URLを共有すると、その論文の主要な情報を自動的に抽出し、Slackスレッド内で要約を提供します。

## 主な機能

- Slackでのメンション（@bot）による論文要約のトリガー
- ArXiv論文の自動解析
- 以下の情報の抽出と表示：
  - 論文タイトル
  - 著者情報
  - カテゴリ
  - 公開日
  - 論文URL
  - PDFリンク
  - 論文の要約

## 技術スタック

### バックエンド言語・フレームワーク
- Python 3.12以上
- Slack Bolt Framework (slack-bolt 1.23.0以上)

### クラウドインフラストラクチャ
- AWS Lambda (サーバーレス実行環境)
- AWS Secrets Manager (機密情報管理)
- Amazon API Gateway (APIゲートウェイ)
- Amazon ECR (コンテナレジストリ)
- AWS SDK (boto3, botocore)
- Amazon CloudWatch (ログ管理・モニタリング)
- AWS IAM (アクセス制御)

### アーキテクチャパターン
- クリーンアーキテクチャ採用
  - domain/ (ドメイン層)
  - usecase/ (ユースケース層)
  - infrastructure/ (インフラ層)
  - di/ (依存性注入)
  - cmd/ (コマンドハンドラー)

### インフラストラクチャ管理
- Terraform (IaC)
- GitHub Actions (CI/CD)

## アーキテクチャ

このBotは以下のような構成で動作します：

1. SlackからのイベントをAWS Lambdaで受信
2. ArXivの論文URLを解析
3. 論文情報を取得し、構造化されたデータに変換
4. Slackスレッド内で整形された形式で情報を表示